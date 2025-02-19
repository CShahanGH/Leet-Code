#Problem Requirements
"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


#Design
"""
Sliding Window by Neetcode
https://www.youtube.com/watch?v=gqXU1UyA8pk
"""

#Implementation Problems and Solutions
"""
I suck at sliding window problems, so I need to practice more 
"""

#Code Start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxf = 0
        maxlength = 0
        count = {} #char:int
        left = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])

            ##Shift left window right if Window length - max frequency > free swaps
            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            maxlength = max(maxlength, right - left + 1)
        
        return maxlength

            







#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = "ABAB"
output = solution.characterReplacement(input, 2)
answer = 4
Test (1, output, answer)

#Test 2
input = "AABABBA"
output = solution.characterReplacement(input, 1)
answer = 4
Test(2, output, answer)

#Test 3
input = "ABAA"
output = solution.characterReplacement(input, 0)
answer = 2
Test(3, output, answer)


