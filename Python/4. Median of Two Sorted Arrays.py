"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10*6 <= nums1[i], nums2[i] <= 10*6
"""

#Idea 
"""
Design on github https://github.com/CShahanGH/Leet-Code/blob/main/Python/Design/Median%20of%20Two%20Sorted%20Arrays.png
Credits to Tushar Roy https://www.youtube.com/watch?v=LPFhl65R7ww&t=369s
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        #To avoid duplicate code I will ensure nums1 is always the shortest array
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
    
        nums1length = len(nums1)
        nums2length = len(nums2)
        totallength = nums1length + nums2length
        start = 0
        end = nums1length
        odd = True if totallength % 2 == 1 else False
        maxnum = 10 ** 6
        minnum = -10 ** 6

        #Find partition for first array (drop decimal)
        nums1partition = (start + end)//2

        #Find Partition for second array (drop decimal)
        nums2partition = (totallength + 1)//2 - nums1partition

        #Continue adjusting the partition until all elements of the left size are <= to all elements on the right side 
        FOUND = False
        while not FOUND:

            #If element is out of bonds on the left side (< 0) set to minnum. If element is out of bonds on the right side (> length) set to maxnum
            maxLeft1 = nums1[nums1partition - 1] if (nums1partition - 1) >= 0 else minnum 
            maxLeft2 = nums2[nums2partition - 1] if (nums2partition - 1) >= 0 else minnum
            minRight1 = nums1[nums1partition] if (nums1partition) < nums1length else maxnum
            minRight2 = nums2[nums2partition] if (nums2partition) < nums2length else maxnum

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                FOUND = True
            elif maxLeft1 > minRight2: #Move partition towards left in nums1
                end = nums1partition - 1
                nums1partition = (start + end)//2
                nums2partition = (totallength + 1)//2 - nums1partition
            else: #Move partition towards right in nums1
                start = nums1partition + 1
                nums1partition = (start + end)//2
                nums2partition = (totallength + 1)//2 - nums1partition
            
        if odd: 
            return max(maxLeft1, maxLeft2)
        else:
            return float(max(maxLeft1, maxLeft2) + min(minRight1, minRight2))/2


        

                
test = Solution()

nums1 = [1, 2]
nums2 = [3, 4]
print(test.findMedianSortedArrays(nums1, nums2))

