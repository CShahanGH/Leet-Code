#Problem Requirements
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


#Design 
"""
Hashing
"""

#Implementation Problems and Solutions
"""
More optimal would be to use a set because you just need one unique key-value
"""

#Code Start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        duplicate = {}
        
        for i in nums:
            if i in duplicate:
                return True
            else:
                duplicate[i] = "skibidi" #Just important to save key
        
        return False 


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



