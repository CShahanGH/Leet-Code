#Problem Requirements

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""



#Design (might be in Design folder)

"""
Z   Z  
Z Z Z    Zigzag row size = 3 
Z   Z  

First Idea: Mark the row the word is in then build the return string by row 
Use a list of lists for each row and append each character based on the row. Pattern for 3. 1,2,3,2,1,2,3 
"""



#Start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rowCount = 1
        strings_by_row = [[] for i in range(numRows)]
        #Give letters a row
        for i in s:
            strings_by_row[rowCount - 1].append(i)
            #Increment or Decrement rowCount
            if numRows == 1:
                increment = 0
            elif rowCount == numRows:
                increment = -1
            elif rowCount == 1:
                increment = 1
            rowCount = rowCount + increment

        #Build String
        answer = ""
        for string in strings_by_row:
            answer = answer + "".join(string)
        return answer


        
      


#Test Code
def Test(program_output, expected_output):
    try:
        assert program_output == expected_output
        return True
    except AssertionError as e: 
        return False


solution = Solution()

#Test 1
string = "PAYPALISHIRING"
numRows = 3
output = solution.convert(string, numRows)
answer = "PAHNAPLSIIGYIR"
if Test(output, answer):
    print("Test 1 passed")
else:
    print("Test 1 failed")

#Test 2
string = "PAYPALISHIRING"
numRows = 4
output = solution.convert(string, numRows)
answer = "PINALSIGYAHRPI"
if Test(output, answer):
    print("Test 2 passed")
else:
    print("Test 2 failed")

#Test 3
string = "A"
numRows = 1
output = solution.convert(string, numRows)
answer = "A"
if Test(output, answer):
    print("Test 3 passed")
else:
    print("Test 3 failed")

#Test 4
string = "ABC"
numRows = 1
output = solution.convert(string, numRows)
answer = "ABC"
if Test(output, answer):
    print("Test 4 passed")
else:
    print("Test 4 failed")