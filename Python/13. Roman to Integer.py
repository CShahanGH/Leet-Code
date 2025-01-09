#Problem Requirements
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


#Design 
"""
Very similar to 12. Integer to Roman but just addition with a few edge cases for 4s and 9s

Too challenge myself I coded only on leet-code so I didn't have intellisence from vscode. 
"""

#Learned
"""
In a standard for loop 'for i in range(0, n) you can't increase the i count in the loop so you have to make a while loop
"""

#Start
class Solution(object):
    def romanToInt(self, s: str) -> int:
        
        #Return number
        number = 0
        #Map each symbol to its int
        symbol_to_int = {
            'I' : 1,
            'IV': 4,
            'V' : 5,
            'IX': 9,
            'X' : 10,
            'XL': 40,
            'L' : 50,
            'XC': 90,
            'C' : 100,
            'CD': 400,
            'D' : 500,
            'CM': 900,
            'M' : 1000
        }

        #Loop through symbols in string - for loop doesn't work 
        symbol = 0
        while symbol < len(s):
            if(s[symbol] == 'I'): #4 and 9 check
                if symbol + 1 < len(s) and s[symbol+1] == 'V':
                    number += symbol_to_int['IV']
                    symbol += 1
                elif symbol + 1 < len(s) and s[symbol+1] == 'X':
                    number += symbol_to_int['IX']
                    symbol += 1
                else: 
                    number += symbol_to_int[s[symbol]]
            elif(s[symbol]  == 'X'): #40 and 90 check
                if symbol + 1 < len(s) and s[symbol+1] == 'L':
                    number += symbol_to_int['XL']
                    symbol += 1
                elif symbol + 1 < len(s) and s[symbol+1] == 'C':
                    number += symbol_to_int['XC']
                    symbol += 1
                else:
                    number += symbol_to_int[s[symbol]]
            elif(s[symbol] == 'C'): #400 and 900 check
                if symbol + 1 < len(s) and s[symbol+1] == 'D':
                    number += symbol_to_int['CD']
                    symbol += 1
                elif symbol + 1 < len(s) and s[symbol+1] == 'M':
                    number += symbol_to_int['CM']
                    symbol += 1
                else:
                    number += symbol_to_int[s[symbol]]
            else: #Default 
                number += symbol_to_int[s[symbol]]

            symbol += 1


        return number



#Testing done on Leetcode for this one




