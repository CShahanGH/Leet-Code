#Problem Requirements
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""


#Design (in design folder)
"""

"""

#Implementation Problems and Solutions
"""
I suck at backtracking implementation
"""

#Code Start
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = ["("]
        res = []

        def backtrack(open, closed):
            if open == closed == n: #Valid match
                res.append("".join(stack))
                return
            
            if closed < open:
                stack.append(")")
                backtrack(open, closed+1)
                stack.pop()
            
            if open < n:
                stack.append("(")
                backtrack(open+1, closed)
                stack.pop() #Remove last append after backtrack finishes
                
            return #Somehow adding this return made it run faster on leetcode


        backtrack(1, 0)

        return res


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert set(output) == set(answer)
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

input = 3
output = solution.generateParenthesis(input)
answer = ["((()))","(()())","(())()","()(())","()()()"]
Test (1, output, answer) 



