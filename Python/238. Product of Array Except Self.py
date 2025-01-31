#Problem Requirements
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


#Design 
"""
Caclulate product of the prefix and suffix of the other elements around the ith element then i = prefix * suffix
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(answer)):
            answer[i] = prefix 
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(answer) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = None
output = None
answer = None

Test (1, output, answer) 



