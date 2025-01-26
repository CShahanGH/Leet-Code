#Problem Requirements
"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


#Design 
"""

"""

#Implementation Problems and Solutions
"""
Couldn't figure out how to count valid parenthesis
https://www.youtube.com/watch?v=HQJL2_73xmA&t=3s
"""

#Code Start
class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] 
        count = 0
        maxcount = 0
            
        for i in range(len(s)):

            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count = i - stack[len(stack)-1] #Current index - index at top of stack
                    if maxcount < count:
                        maxcount = count

        return maxcount


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



