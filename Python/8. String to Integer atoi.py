#Problem Requirements
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. 
Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42

Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:
Input: s = " -042"
Output: -42

Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:
Input: s = "1337c0d3"
Output: 1337

Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:
Input: s = "0-1"
Output: 0

Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
        ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^

Example 5:
Input: s = "words and 987"
Output: 0

Explanation:
Reading stops at the first non-digit character 'w'.

Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""

#Design (might be in Design folder)
"""
The problem is kind enough to give the algorithim behind atoi so let's try and implement it 
"""

#Start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        #Fail Fast
        if s == None or s == "" or s == " ":
            return ans

        #For checking if a character in string is an int
        string_to_int = {
                            "0": 0,
                            "1": 1,
                            "2": 2,
                            "3": 3,
                            "4": 4,
                            "5": 5,
                            "6": 6,
                            "7": 7,
                            "8": 8,
                            "9": 9,
        }

        #1. Ignore White Space
        while s[0] == " ":
            s = s[1:]
        
        #2. Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
        sign = -1 if s[0] == "-" else 1
        
        #Trim - or + sign
        if s[0] == "-" or s[0]== "+":
            s = s[1:]

        #3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
        # If no digits were read, then the result is 0.

        #3.1. Ignore Leading Zeroes
        while s[0] == "0":
            s = s[1:]
        
        print(s)

        #3 Read integer similar to the reverse integer problem but stop when no longer an integer
        for i in range (0, len(s)):
            if s[i] not in string_to_int:
                break
            ans = ans * 10
            ans = ans + string_to_int[s[i]]

        #Set Sign 
        ans = ans * sign

        #4 Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. 
        if ans < INT_MIN:
            ans = INT_MIN
        elif ans > INT_MAX :
            ans = INT_MAX 
            
        return ans
        

        


#Test Code
def Test(program_output, expected_output):
    try:
        assert program_output == expected_output
        return True
    except AssertionError as e: 
        return False


solution = Solution()


#Test 1
input = "42"
output = solution.myAtoi(input)
answer = 42
if Test(output, answer):
    print("Test 1 passed")
else:
    print(f"Test 1 failed got {output} expected {answer}")

#Test 2
input = " -042"
output = solution.myAtoi(input)
answer = -42
if Test(output, answer):
    print("Test 2 passed")
else:
    print(f"Test 2 failed got {output} expected {answer}")

#Test 3
input = "1337c0d3"
output = solution.myAtoi(input)
answer = 1337
if Test(output, answer):
    print("Test 3 passed")
else:
    print(f"Test 3 failed got {output} expected {answer}")

#Test 4
input = "0-1"
output = solution.myAtoi(input)
answer = 0
if Test(output, answer):
    print("Test 4 passed")
else:
    print(f"Test 4 failed got {output} expected {answer}")

#Test 5
input = "words and 987"
output = solution.myAtoi(input)
answer = 0
if Test(output, answer):
    print("Test 4 passed")
else:
    print(f"Test 5 failed got {output} expected {answer}")