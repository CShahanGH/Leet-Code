#Problem Requirements
"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


#Design (might be in Design folder labeled problem number)
"""
Use two hash_maps
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range (len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1 #get returns value at key or a default value
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        
        return s_dict == t_dict


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



