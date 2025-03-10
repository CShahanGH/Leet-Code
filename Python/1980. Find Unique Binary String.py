#Problem Requirements
"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
"""


#Design
"""
Flip bits in a diagonal
"""

#Implementation Problems and Solutions
"""
My first backtracking attempt solutution sucked, so I still need to work on backtracking=
"""

#Code Start
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        ans = ""
        for i in range(len(nums)):
            if nums[i][i] == "1":
                ans += "0"
            else:
                ans += "1"
        
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
input = ["00", "01"]
output = solution.findDifferentBinaryString(input)
print(output)



