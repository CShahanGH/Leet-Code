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

#Attempt 1
"""
Too Long 
seen = []

        if s not in seen:
            seen.append(s)
            if self.isPalindrome(s):
                return s
        
        endslice = s[:-1] #Slice the end of the string
        startslice = s[1:] #Slice the beginning of the string
        
        endsubstring = self.longestPalindrome(endslice)
        startsubstring = self.longestPalindrome(startslice)

        if len(endsubstring) > len(startsubstring):
            return endsubstring
        else:
            return startsubstring
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #For each character 
        longestpalindrome = ""
        for i in range(len(s)):
            #Odd example 1
            left = i
            right = i 
            palindrome = self.findPalindrome(s, left, right)
            if len(palindrome) > len(longestpalindrome):
                longestpalindrome = palindrome
            #Even example 2
            left = i
            right = i+1
            palindrome = self.findPalindrome(s, left, right)
            if len(palindrome) > len(longestpalindrome):
                longestpalindrome = palindrome
        return longestpalindrome
    
    #Compare elements left and right
    def findPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(s[left+1:right])
        return s[left+1:right] #return the two slices of the palindrome toghether 
            
                



           

        

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

#Example 3 Test
s = "racecar"
output = test.longestPalindrome(s)
testoutput = ["racecar"]
if testLongestPalindrome(output, testoutput):
    print("Test 3 pass")
else:
    print("Test 3 Fail")

#Example 4 Test
s = "dbbd"
output = test.longestPalindrome(s)
testoutput = ["dbbd"]
if testLongestPalindrome(output, testoutput):
    print("Test 4 pass")
else:
    print("Test 4 Fail")
