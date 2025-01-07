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
You can look at my attempt in the design folder and old code, but this top-down solution comes from Neet Code
"""

#Start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        index_map = {} #Memoize indexes for repeated calculations 
        #Recursive DFS  
        def dfs (sp, pp):

            if (sp, pp) in index_map:
                return index_map[(sp, pp)]
            if sp >= len(s) and pp >= len(p): #String and Pattern Matched
                return True
            if sp < len(s) and pp >= len(p): #String has text left over so match
                return False

            
            match = sp < len(s) and (s[sp] == p[pp] or p[pp] == ".") #True if Match False if No Match - Can't compute if string is out of bounds
            
            if pp + 1 < len(p) and p[pp+1] == "*": #p[0] will never be a star but pp+1 might be out of bounds - will be true if next pp is *
                index_map[(sp, pp)] = dfs(sp, pp+2) or match and dfs(sp+1, pp)  #skip the * or use the char before the * #MEMOIZE
                return index_map[(sp, pp)]
            if match:
                index_map[(sp,pp)] = dfs(sp+1, pp+1) #MEMOIZE
                return index_map[(sp, pp)]

            index_map[(sp, pp)] = False #MEMOIZE
            return index_map[(sp, pp)]
                
        #Start dfs at 0 indexes
        return dfs(0, 0)
    
#Old Code
"""
 sp = 0 #string index pointer
        pp = 0 #pattern index pointer

        while sp < len(s) and pp < len(p):
            if p[pp] == s[sp] or p[pp] == ".": #Move both best case a = a
                pp += 1
                sp += 1
            elif p[pp] != s[sp] and p[pp] != "*": # a = b 
                #Try for Zero Star
                pp += 1
                if pp >= len(p): #Out of Bonds Not Match
                    return False 
                if p[pp] != "*":
                    return False #No * to make zero *
                else:
                    pp += 1
                    #MAYBE A BOUNDS CHECK
            else: #pp-> *
                starp = pp
                
                #CASE WHEN * is ONLY ONE OF THE PREVIOUS ELEMENT
                if pp + 1 < len(p):
                    if p[pp + 1] == s[sp] and s[sp] == p[pp - 1] or p[pp + 1] == ".": #RAAAAAAAAAAAA

                        #RANOM CHECK for ".*.." HEHEHEHEHE meaing *. is 0
                        if pp + 2 < len(p):
                            if p[pp+1] == p[pp+2] or p[pp+2] == ".":
                                pp += 2 #SKIP BOFA
                        sp += 1
                        pp += 1
                        continue #Continue to top loop
                    

                #0* star loop
                while pp <len(p):
                    pp += 1
                    if pp >= len(p): #Out of bounds failed 0* try next check after loop
                        pp -= 1 #STUPID should not be s[sp]
                        break
                    if p[pp] != s[sp] and p[pp] != ".": #Go for *
                        pp += 1
                        if pp >= len(p): #Out of bounds failed 0* try next check after loop
                            pp -= 1 #STUPID should be s[sp]
                            break
                        if p[pp] != "*":
                            pp -= 1 #STUPID should be s[sp]
                            break
                        else: #pp->* continue zero star check
                            continue
                    else: #p[pp] == s[sp] break and continue top loop

                        starp2 = pp
                        #ANOTHER 0 STAR FILTER BECAUSE WHY NOT
                        while pp < len(p):
                            if p[pp] != "*": #Go for star
                                pp += 1
                                if pp >= len(p): #Out of bounds failed 0* return False for leftover pattern not matche 
                                    pp -= 1
                                    break
                                if p[pp] != "*":  #Still no star match not found
                                    pp -= 1
                                    break
                            else: #pp -> *
                                pp += 1
                        if p[pp] != p[starp2]:
                            pp = starp2
                        break #AAAAAAAA
                if p[pp] == s[sp] or p[pp] == ".": 
                    continue #Go to top loop
                #0* loop failed try previous pp multiple times
                pp = starp
                pp = pp - 1 #DON'T CARE 
                if p[pp] != s[sp] and p[pp] != ".": #Preceeding element does not match
                    return False
                

        #CleanUp
        if sp != len(s): #String not matched complete
            return False 

        
        #Todo Cleanup Leftover Zero*s 
        while pp < len(p):
            if p[pp] != "*": #Go for *
                pp += 1
                if pp >= len(p): #Out of bounds failed 0* return False for leftover pattern not matche 
                    return False 
                if p[pp] != "*":  #Still no star match not found
                    return False
            if pp + 1 < len(p):
                    pp += 1
            else: #pp -> *
                pp += 1

        return True #If the pattern survived all the checks return true
"""
#Test Code
def Test(program_output, expected_output):
    try:
        assert program_output == expected_output
        return True
    except:
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
inputstring = "aaaaaa"
inputpattern = "a*a*a*"
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

#Test 12
inputstring = "mississippi"
inputpattern = "mis*is*ip*."
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 12 passed")
else:
    print(f"Test 12 failed got {output} expected {answer}")

#Test 13
inputstring = "bbba"
inputpattern = ".*a*a"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 13 passed")
else:
    print(f"Test 13 failed got {output} expected {answer}")

#Test 14
inputstring = "aaca"
inputpattern = "ab*a*c*a"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 14 passed")
else:
    print(f"Test 14 failed got {output} expected {answer}")

#Test 15
inputstring = "aa"
inputpattern = "a*aa"
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 15 passed")
else:
    print(f"Test 15 failed got {output} expected {answer}")

#Test 16
inputstring = "a"
inputpattern = ".*."
output = solution.isMatch(inputstring, inputpattern)
answer = True
if Test(output, answer):
    print("Test 16 passed")
else:
    print(f"Test 16 failed got {output} expected {answer}")
