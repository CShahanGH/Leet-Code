#Problem Requirements
"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""


#Design (might be in Design folder labeled problem number)
"""
Very similar to previous Palindrome problems instead we are dealing with integers and not strings 

Negative numbers are not palindromes 

To avoid converting the integer into a string we can probably divide the integer into a stack by dividing it by 10 since we are in the decimal system and caputring it's remainder. 

Ex 121. 

121 / 10 = 12.1. 1 goes in the 1's spot -> push 1 onto the stack
12 / 10 = 1.2. 2 goes in the 10's spot -> push 2 onto the stack
1 / 10 = .1 1 goes in the 100's spot -> push 1 onto the stack 

Then check if the length of the stack is even or odd for implementing the palindrome 

Check if it's a palindrome similar to the helping function in 5. Longest Palindromic Substring 

    #Compare elements left and right
        def findPalindrome(self, s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            print(s[left+1:right])
            return s[left+1:right] #return the two slices of the palindrome toghether 

At any point the number isn't a palindrome return false
"""

#Start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """


#Test Code
def Test(program_output, expected_output):
    try:
        assert program_output == expected_output
        return True
    except AssertionError as e: 
        return False


solution = Solution()

#Test 1

input = None
output = None
answer = None

if Test(output, answer):
    print("Test 1 passed")
else:
    print(f"Test 1 failed got {output} expected {answer}")

