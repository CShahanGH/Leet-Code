#Problem Requirements
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


#Design (might be in Design folder labeled problem number)
"""
For each string in the input string, I want to compare each of their characters. 

Compare the current char of the 0th string with the current char of the ith string. 
"""

#Learned
"""
Thinking about loops within loops is still hard, and always remember to test input extremes
"""

#Code Start
from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #One String in list
        if len(strs) == 1:
            return strs[0]


        prefix = ""

        #Loop until first index fails or match stops
        i = 0 
        inbounds = True #Set to false on index out of bounds
        match = True #Set to false when indexes don't match

        while inbounds and match: #Loop string index
            for s in range(1, len(strs)): #Loop strings past the 1st
                if(i < len(strs[s]) and i < len(strs[0])): #Check bounds
                    
                    if strs[0][i] != strs[s][i]: #Compare first string char with other strings char
                        match = False

                else:
                    inbounds = False
            
            if match and inbounds:
                prefix += strs[0][i]

            i = i + 1 

        return prefix


#Test Code
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = ["flower","flow","flight"]
output = solution.longestCommonPrefix(input)
answer = "fl"
Test (1, output, answer) 

#Test 2
input = ["dog","racecar","car"]
output = solution.longestCommonPrefix(input)
answer = ""
Test (2, output, answer) 

#Test 3
input = [""]
output = solution.longestCommonPrefix(input)
answer = ""
Test (3, output, answer) 