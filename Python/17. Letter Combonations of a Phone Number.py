#Problem Requirements
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


#Design (in Design Folder)
"""
Credit to Neetcode
"""

#Implementation Problems and Solutions
"""
I need to get better at determing what type of algorithmic problem a question is.

I know leetcode can say a topic, but the topic kinda gives the algorithim away

I had forgotten how to implement a backtracking aglorithim
"""

#Code Start
from typing import List


class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:

        combos = [] 
        
        phone_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        #Neetcode Magic
        def backtrack(index, combo):
            if len(combo) == len(digits):
                combos.append(combo)
                return
            
            for c in phone_map[digits[index]]:
                backtrack(index + 1, combo + c)
        
        if digits != "":
            backtrack(0, "")
        
        return combos


#Test Code
def Test(id, output, answer):
    try:
        assert set(output) == set(answer)
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = "23"
output = solution.letterCombinations(input)
answer = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Test (1, output, answer) 


