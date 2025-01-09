#Problem Requirements
"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX.
Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. 
You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

Example 1:
Input: num = 3749
Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:
Input: num = 58
Output: "LVIII"

Explanation:
50 = L
 8 = VIII

Example 3:
Input: num = 1994
Output: "MCMXCIV"

Explanation:
1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Constraints:

1 <= num <= 3999

"""

#Design
"""
My first idea is to subtract the number by the largest numeral is possible. Keep a count of each number. Save Symbol as a string or char in a hashmap. 

First design worked but was slow. 

We can just iterate through the symbol's integer values and append the symbol(s) to the string.

Second design works much faster than 1st
"""

#Code Start
class Solution(object):
    def intToRoman(self, num: int) -> str:

        Roman = "" #answer string

        #Map into to symbol
        int_to_symbol = {
            1000 : 'M',
            900 :'CM',
            500 : 'D',  
            400 : 'CD',
            100 : 'C',
            90 : 'XC', 
            50 : 'L', 
            40 : 'XL',
            10 : 'X', 
            9 : 'IX', 
            5 : 'V', 
            4 : 'IV',
            1 : 'I', 
        }

        #Loop through each symbol
        for i in int_to_symbol:
            while num >= i: #Subtract largest symbol from the number
                num -= i
                Roman += int_to_symbol[i] #Append the numberal to the string

        return Roman

#Test Code
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = 3749
output = solution.intToRoman(input)
answer = "MMMDCCXLIX"
Test (1, output, answer) 

#Test 2
input = 58
output = solution.intToRoman(input)
answer = "LVIII"
Test (2, output, answer) 

#Test3
input = 1994
output = solution.intToRoman(input)
answer = "MCMXCIV"
Test (3, output, answer) 