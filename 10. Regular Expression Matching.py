#Problem Requirements
"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

#Design (In Design Folder)
"""
I know this solution is stupid and will learn the best solution eventually
"""

#Start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sp = 0 #string index pointer
        pp = 0 #pattern index pointer
        lock = 0 #Used for tracking the previous matching * element 

        #This is going to be ugly cound that I might condense later and reverse the logic later
        while sp < len(s) and pp < len(p):
            if s[sp] == p[pp] or p[pp] == ".": #Move both
                sp += 1
                pp += 1
                continue
            if s[sp] != p[pp] and p[pp] != "*": #Try forward p for star
                pp += 1
                if pp >= len(p): #End of pattern reached
                    continue
                if p[pp] == "*": #Continue to star check
                    continue
                return False #pattern will not match 
            if p[pp] == "*": #Queue backrooms music
                #Save previous character and pointer for duplicate elements
                if p[pp-1] == s[sp] and lock == 0:
                    lock = 1
                    pplock = pp #Lock the pp
                #Preceding elements till end string of string
                if lock == 1:
                    sp += 1
                    pp = pplock
                    lock = 0
                if sp >= len(s): #End of string reached
                    continue  
                #Check for zero* or match by moving p forward
                pp += 1
                if pp >= len(p): #End of pattern reached
                        continue
                #Match first
                if p[pp] == s[sp]:
                    continue 
                #Find zero* 
                if p[pp] != s[sp]:
                    pp += 1
                    if pp >- len(p): #End of pattern reached
                        continue
                    if p[pp] == "*": #Star found
                        continue


                    
        
        #When pattern ends early
        if pp >= len(p):
            #Empty string
            while sp < len(s):
                if p[len(p) - 1] != "*":
                    return False
                if s[sp] != p [len(p) - 2] and p[len(p)-2] != ".": #Char before star "hopefully ** doesn't count"
                    return False
                sp += 1

        #When String ends early
        if sp >= len(s): #empty ending 0 *'s in pattern
            count = 0
            while pp < len(p):
                if p[pp] == "*":
                    pp += 1
                else: # p[pp] != "*":
                    if pp + 1 < len(p): #Check next p for star
                        pp += 1
                        if p[pp] != "*":
                            return False #No 0 star 
                        pp += 1
                        continue
                    return False #No stars 
                     
        return True




#Test Code
def Test(program_output, expected_output):
    try:
        assert program_output == expected_output
        return True
    except AssertionError as e: 
        return False


solution = Solution()

#Test 1
inputstring = "aa"
inputpattern = "a"
output = solution.isMatch(inputstring, inputpattern)
answer = False
if Test(output, answer):
    print("Test 1 passed")
else:
    print(f"Test 1 failed got {output} expected {answer}")

#Test 2
inputstring = "aaaaaa"
inputpattern = "a*"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 2 passed")
else:
    print(f"Test 2 failed got {output} expected {answer}")

#Test 3
inputstring = "ab"
inputpattern = ".*"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 3 passed")
else:
    print(f"Test 3 failed got {output} expected {answer}")

#Test 4
inputstring = "aab"
inputpattern = "c*a*b"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 4 passed")
else:
    print(f"Test 4 failed got {output} expected {answer}")

#Test 5
inputstring = "abcd"
inputpattern = "d*"
output = solution.isMatch(inputstring, inputpattern)
answer = False
if Test(output, answer):
    print("Test 5 passed")
else:
    print(f"Test 5 failed got {output} expected {answer}")

#Test 6
inputstring = "ab"
inputpattern = ".*c"
output = solution.isMatch(inputstring, inputpattern)
answer = False
if Test(output, answer):
    print("Test 6 passed")
else:
    print(f"Test 6 failed got {output} expected {answer}")

#Test 7
inputstring = "aaa"
inputpattern = "ab*a*c*a"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 7 passed")
else:
    print(f"Test 7 failed got {output} expected {answer}")

#Test 8
inputstring = "aaaaaaaaaaaaaaaab"
inputpattern = "ab*ac*a*"
output = solution.isMatch(inputstring, inputpattern)
answer = False
if Test(output, answer):
    print("Test 8 passed")
else:
    print(f"Test 8 failed got {output} expected {answer}")

#Test 9
inputstring = "abc"
inputpattern = "abcd*e*f*"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 9 passed")
else:
    print(f"Test 9 failed got {output} expected {answer}")

#Test 10
inputstring = "aaa"
inputpattern = "a*a"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 10 passed")
else:
    print(f"Test 10 failed got {output} expected {answer}")

#Test 11
inputstring = "aaa"
inputpattern = "aaaa"
output = solution.isMatch(inputstring, inputpattern)
answer = False
if Test(output, answer):
    print("Test 11 passed")
else:
    print(f"Test 11 failed got {output} expected {answer}")

