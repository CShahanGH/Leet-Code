#Problem Requirements
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


#Design
"""
Credit Neetcode
Locate sequence start by searching for current_ele - 1 in list O(n) with list or O(1) with set 
Find sequence end same way except current_ele + 1
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        max_length = 0
        for num in num_set:
            length = 1

            if num - 1 in num_set: #Not a sequence start
                continue 
            else: #Sequence start
                while num + 1 in num_set: #Find next
                    num = num + 1
                    length += 1
                
                max_length = max(length, max_length)
        
        return max_length



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



