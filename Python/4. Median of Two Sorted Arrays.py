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
For logrithmic time I need to use a divide and conquer strategy. 

We need to check if the two arrays combined is even or odd becasue if the combined array is old the median is in the middle, but if the array is even the median is the middle two digits/2

We need to calculate the midpoint of each array.

Compare midpoints and remove a partion of an array.

We need to recalculate the midpont of each array so we might want to use a recursive function 

helper(mid, nums1, nums2)
{
base case when: return nums1[mid] or return nums2[mid]

recuse
helper(new mid, new nums1, nums2)
or 
helper(new mid, nums1, new nums2)
}


"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalsize = len(nums1) + len(nums2)

        odd = True if totalsize % 2 == 1 else False

        #Floor Division
        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2



       

         
    
                
test = Solution()

nums1 = [1,2]
nums2 = [3,4]
print(test.findMedianSortedArrays(nums1, nums2))

