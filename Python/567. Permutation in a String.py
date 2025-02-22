#Problem Requirements
"""
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


#Design
"""
Hashmap and sliding window
"""

#Implementation Problems and Solutions
"""
Debugger was my best friend, but ew might revisit for a cleaner solution
"""

#Code Start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_map = {}
        k, left, right =0, 0, 0 #Sliding Window Variables

        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        while right < len(s2):

            if s2[right] in s1_map: #Permutation valid

                s1_map[s2[right]] -= 1

                #Duplicate in permutation found
                if s1_map[s2[right]] == -1:
                    
                    #Adjust window by 1
                    if s2[left] == s2[right]:
                        s1_map[s2[left]] += 1
                        left += 1
                        k -= 1
                    else:
                        #Adjust left to next instance of right char in string (not always left == right)
                        while s2[left] != s2[right]:
                            s1_map[s2[left]] += 1
                            left += 1
                            k -= 1
                        #Adjust window by 1
                        if s2[left] == s2[right]:
                            s1_map[s2[left]] += 1
                            left += 1
                            k -= 1
    
                right += 1
                k += 1
            
            else: #Reset window

                while left != right: 
                    s1_map[s2[left]] += 1 #Should be valid
                    left += 1
            
                left = right +1
                right = left
                k = 0
            
            
            #If window size = s1 length Permuation valid
            if k== len(s1):
                return True
            
        return False


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = "ab"
input2 = "eidboaoo"
output = solution.checkInclusion(input, input2)
answer = False

Test (1, output, answer) 



