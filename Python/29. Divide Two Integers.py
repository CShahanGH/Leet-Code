#Problem Requirements
"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


#Design (in Design Folder)
"""
Power's of 2 idea from https://www.youtube.com/watch?v=pBD4B1tzgVc
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        #Leave Fast
        if dividend == divisor:
            return 1

        #Capture Sign
        negative = False
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            negative = True

        #Convert to positive by doing bitwise not + 1
        if dividend < 0:
            dividend = ~dividend + 1
        
        if divisor < 0:
            divisor = ~divisor + 1

        ans = 0
        while (dividend >= divisor):
            
            #Find the largest x where divisor * 2^x < dividend
            x = 0
            divisor_times_two_to_x = divisor * 2**x
            while(dividend - divisor_times_two_to_x > divisor_times_two_to_x): #Leave at case before divisor > dividend -> (dividend > divisor_times_two_to_x) results in x being 1 too big
                x += 1
                divisor_times_two_to_x = divisor * 2**x

            dividend = dividend - divisor_times_two_to_x
            ans += 2**x

        #Convert back to negative
        if negative:
            ans = ~ans + 1
        
        #Quotient Edge Cases
        if (ans > 2**31 - 1):
            return 2**31 - 1
        elif(ans < -2**31):
            return -2**31
        else:
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
input = None
output = None
answer = None

Test (1, output, answer) 



