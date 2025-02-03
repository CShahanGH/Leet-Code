#Problem Requirements
"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""


#Design
"""
Stack and Function dictionary
"""

#Implementation Problems and Solutions
"""
I was using floor division x//y  instead of int divison int(x/y) and was losing my mind
"""

#Code Start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def add():
            right  = stack.pop()
            left = stack.pop()
            result = left + right
            stack.append(result)

        def subtract():
            right  = stack.pop()
            left = stack.pop()
            result = left - right
            stack.append(result)
        
        def multiply():
            right  = stack.pop()
            left = stack.pop()
            result = left * right
            stack.append(result)

        def divide():
            right  = stack.pop()
            left = stack.pop()
            result = int(left/right)
            stack.append(result)

        stack = []

        function_dict = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide,
        }

        for token in tokens:

            if token in function_dict:
                function_dict[token]()
            else:
                stack.append(int(token))
        
        return stack.pop()
    
    


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
output = solution.evalRPN(input)
answer = 22

Test (1, output, answer) 



