#Problem Requirements
"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


#Design (in Design Folder)
"""

"""

#Implementation Problems and Solutions
"""
mississippi - Using a normal for loop for the haystack will pass over the 4th i for the needle "issip"
"""

#Code Start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        ans = -1
        n = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[n]: #
                if n == 0: #Capture index at first n
                    ans = i
                n += 1
                if n == len(needle):
                    return ans
            else:
                n = 0
                if ans != -1:
                    i = ans #Reset i if needle failed
                    ans = -1
            i += 1
        return -1

#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")

solution = Solution()
#Test 1
input = "mississippi"
input2 = "issip"
output = solution.strStr(input, input2)
answer = 4

Test (1, output, answer) 



