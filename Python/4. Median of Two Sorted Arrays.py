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
-106 <= nums1[i], nums2[i] <= 106
"""

#Idea 
"""
Return fast, Cover edge cases such as empty arrays, or single number arrays

Make a new array with the sorted values and 



Ex. [1,2,3,4,5] [3,4]
Odd Length
Mid = 3, 3 

Return 3

Ex. [1, 3, 4, 5, 6] [7, 8, 9, 12]

median = 6 

Odd length 

Mid = 4, 9



"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        if len(nums1) == 0 and len(nums2) == 1:
            return nums2[0]

        if len(nums1) == 1 and len(nums2) == 0:
            return nums1[0]
        
        merge = []

        inums1 = 0
        inums2 = 0
        while True: 
            if inums1 > len(nums1) - 1 and inums2 > len(nums2) - 1:
                break
            if inums1 > len(nums1) - 1:
                merge.append(nums2[inums2])
                inums2 = inums2 + 1
                continue
            if inums2 > len(nums2) - 1:
                merge.append(nums1[inums1])
                inums1 = inums1 + 1
                continue
            if nums1[inums1] < nums2[inums2]:
                merge.append(nums1[inums1])
                inums1 = inums1 + 1
            else: 
                merge.append(nums2[inums2])
                inums2 = inums2 + 1

            
        odd = True if len(merge) % 2 != 0 else False 

        if odd:
            return merge[int(len(merge)/2)]
        else:
            return (merge[int(len(merge)/2)] + merge[int(len(merge)/2) - 1])/2
            



        
            
            
                

test = Solution()

nums1 = [1,2]
nums2 = [3,4]
print(test.findMedianSortedArrays(nums1, nums2))

