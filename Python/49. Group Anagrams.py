#Problem Requirements
"""
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


#Design 
"""
Use a dictionary {char_count:list[str]}
"""

#Implementation Problems and Solutions
"""
Credit to Neetcode
"""

#Code Start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for s in strs:

            #Count characters in s using AscII code
            count = [0] * 26 #a-z 
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count) 

            #Add to result hash_map
            result[key] = result.get(key, []) + [s]
        #Return hash_map values as a list
        return list(result.values())


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



