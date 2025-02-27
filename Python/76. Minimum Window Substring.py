#Problem Requirements
"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""


#Design
"""
Hashmap with char count 
Queue with next left pointer 
Iterate through s string and expand right pointer until end of array
-Capture any valid substrings
--Probably a better way
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #Fail Fast 
        if len(s) < len(t):
            return ""
        
        ans = ""
        char_count = {}
        left_queue = []
        min = len(s)
        count = 0 
        left = -1

        for char in t:
            char_count[char] = char_count.get(char, 0) + 1
        
        for right in range(len(s)):

            if s[right] in char_count:

                #Update left
                if left == -1:
                    left = right
                else:
                    left_queue.append(right)
                
                #Update char count
                char_count[s[right]] -= 1
                if char_count[s[right]] >= 0:
                    count += 1
                
                #Valid substring found
                while count == len(t):

                    #Calculate Window Size
                    k = right - left + 1

                    #Update Min
                    if k <= min:
                        ans = s[left:right+1]
                        min = k
                        if min == len(t): #Win fast
                            return ans

                    #Update Count
                    char_count[s[left]] += 1
                    if char_count[s[left]] > 0:
                        count -= 1

                    #Update Left
                    if left_queue:
                        left = left_queue.pop(0)
                    else:
                        left = -1
        
        return ans


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = "ADOBECODEBANC"
input2 = "ABC"
output = solution.minWindow(input, input2)
answer = "BANC"

Test (1, output, answer) 



