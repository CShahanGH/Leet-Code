#Problem Requirements
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

#Design
"""
Binary Search ignoring the sorted side
"""

#Implementation Problems and Solutions
"""
Needed to check left and right for possible min value as well as the mid vale
"""

#Code Start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums) - 1
        ans = min(nums[left], nums[right])

        while left <= right:

            mid = left + (right - left) // 2
            
            ans = min(ans, nums[mid])
            ans = min(ans, nums[right])
            ans = min(ans, nums[left])

            if nums[mid] > nums[left] and nums[mid] < nums[right]: #Normal rotation
                return ans

            if nums[mid] < nums[left] and nums[mid] < nums[right]: #Mid to right sorted - make right mid - 
                right = mid - 1
            else: #Left to mid sorted
                left = mid + 1
        
        return ans
            





#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [3, 4, 5, 1, 2]
output = solution.findMin(input)
answer = 1
Test (1, output, answer) 



