"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# Initial Idea 
"""
Counter and max count variable starts at 1
Loop through the length of the string. 
Record the current char in an array or list
If the current char not in list increment counter. 
If next char in list reset counter.
"""

#Final Solution 
"""
2 Edge cases for empty input

Max length starts at one for single character inputs 
charlist starts witht the first chracter 
loop through the string starting after the first character
if the charcter isn't in the list append it to the list
if the character is in the list. pop elements from the front of the list until list has no more of the same char. then add the char to the list 

maxlength is the length of the longest list. 

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return 0
        if s == " ":
            return 1

        maxlength = 1
        charlist = [s[0]]
        for c in s[1:]:
            if c not in charlist:
                charlist.append(c)
            else:
                while c  in charlist:
                    charlist.pop(0)
                charlist.append(c)
            if(maxlength < len(charlist)):
                maxlength = len(charlist)

        return maxlength
        

test = Solution()

print(test.lengthOfLongestSubstring("dvdf"))
print(test.lengthOfLongestSubstring("abcabcbb"))
print(test.lengthOfLongestSubstring("bbbbb"))
print(test.lengthOfLongestSubstring("pwwkew"))


