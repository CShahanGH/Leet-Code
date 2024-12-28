"""
Given a string s, return the longest 
palindromic substring in s.

 Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    
def testLongestPalindrome(output, testoutput):
    """
    :type s: str
    :type test: list[str]
    :rtype: bool
    """
    try:
        assert output in testoutput
        return True
    except AssertionError as e: 
        return False

test = Solution() 

#Example 1 Test
s = "babad"
output = test.longestPalindrome(s)
testoutput = ["bab", "aba"]
if testLongestPalindrome(output, testoutput):
    print("Test 1 pass")
else:
    print("Test 1 Fail")

#Example 2 Test
s = "cbbd"
output = test.longestPalindrome(s)
testoutput = ["bb"]
if testLongestPalindrome(output, testoutput):
    print("Test 2 pass")
else:
    print("Test 2 Fail")
