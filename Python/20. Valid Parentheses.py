#Problem Requirements
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


#Design
"""
I feel like I just need to use a hash_map

My topics: hashmap, String
Problem topics: String, Stack

Yep, I misunderstood the problem. Each paraenthese needs to be in a valid order too.

s "([[{]})]])" is not valid

we can add '([{' to a stack but when ')]}' is the char we pop the stack and if it's not matching we return false

I'm still going to use a hash_map for matching symbols
"""

#Implementation Problems and Solutions
"""
Submission failed 2 times because I forgot to account for an empty stack being popped otherwise it was perfect
"""

#Code Start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        match = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for p in s:
            #Open parentheses
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            else: #Match
                if len(stack) > 0:
                    mp = stack.pop()
                    if mp != match[p]:
                        return False
                else:
                    return False

        #Stack should be empty
        if len(stack) > 0:
            return False
        return True


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = "()"
output = solution.isValid(input)
answer = True
Test (1, output, answer) 

#Test 2
input = "()[]{}"
output = solution.isValid(input)
answer = True
Test (2, output, answer) 

#Test 3
input = "(]"
output = solution.isValid(input)
answer = False
Test (3, output, answer) 

#Test 4
input = "([])"
output = solution.isValid(input)
answer = True
Test (4, output, answer) 