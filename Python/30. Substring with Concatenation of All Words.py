#Problem Requirements
"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""


#Design
"""
TODO Study sliding window
"""

#Implementation Problems and Solutions
"""
I'm tired so I will study someone else's solution https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/1753357/clear-solution-easy-to-understand-with-diagrams-o-n-x-w-approach/
"""

#Code Start
from collections import defaultdict
from typing import Counter, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsCount = Counter(words)
        n, wordLen = len(s), len(words[0])
        totalLen = wordLen * len(words)
        ans = []

        # we need to traverse s worldLen times
        for i in range(wordLen):
            curCount = defaultdict(int)

            # tarverse s with diff beginning index
            for j in range(i, n-wordLen+1, wordLen):

                # hashing a worldLen len string
                if s[j:j+wordLen] in wordsCount:
                    curCount[s[j:j+wordLen]] += 1

                # subtract a worldLen len string if the string in words
                if j >= totalLen and s[j-totalLen: j-totalLen+wordLen] in wordsCount:
                    curCount[s[j-totalLen: j-totalLen+wordLen]] -= 1

                if curCount == wordsCount:
                    ans.append(j-totalLen+wordLen)
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
input = "barfoothefoobarman"
input2 = ["foo","bar"]
output = solution.findSubstring(input, input2)
answer = [0,9]

Test (1, output, answer) 



