"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

#Design
"""
Store length of string and delimiter in string
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
from typing import List


class Solution(object):

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "," + s
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        
        res_list = []
        index = 0
        while index < len(s):

            #Read number
            length = 0
            while s[index] != ",":
                length *= 10 #For increasing digits place
                length += int(s[index])
                print(s[index])
                index += 1

            index += 1 #Skip delimiter

            #Build string
            string = ""
            for _ in range(length):

                char = s[index]
                string += char
                index += 1
            
            #Add string to list
            res_list.append(string)
        
        return res_list







#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = ["we","say",":","yes","!@#$%^&*()"]
output = solution.encode(input)
output2 = solution.decode(output)
answer = None

Test (1, output, answer) 