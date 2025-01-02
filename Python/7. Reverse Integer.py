#Problem Requirements
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 
Constraints:

-2^31 <= x <= 2^31 - 1
"""


#Design (might be in Design folder)
"""
Considering bit manipulation: signed 32-bit integer's are represented in two's complement notation. Range (-2,147,483,648 , 2,147,483,647) (-2^31 to 2^31-1)

Representing ints as bits in two's complement notation:

Binary min = 10000000000000000000000000000000
Binary max = 01111111111111111111111111111111

Let's see if we can transform 123 to 321

123 binary = 0000000001111011
321 binary = 0000000101000001

I don't see anything but would be cool if I could use bit manipulation because I want more practice on it. 

I could convert the integer to a string and reverse the string but thats lame

After quickly searching the internet for ideas I think I saw someone maipulating the decimal system -> base 10 

Back to example 1 
123/10 = 12.3 -> 3  
12/10 = 1.2 -> 2
1/10 = .1 -> 1

Cool we can store the reaminder of the number to reverse it 
300 + 20 + 1 = 321

reverse(number)
    start answer at 0
    Begin loop
    ans = ans * 10 -> increase decimal place 
    remainder = number % 10
    ans = ans + remainder 
    number = number floor 10 (number // 10) -> drop the decimal
    if number > 0 return to loop start
    return ans 

Need to capture sign 

"""



#Start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            ans = ans * 10
            remainder = x % 10
            ans = ans + remainder
            x = x // 10
        ans = ans * sign

        #Check bounds 
        if ans < -2**31 or ans > (2**31 - 1):
            return 0
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
input = 123
output = solution.reverse(input)
answer = 321
if Test(output, answer):
    print("Test 1  passed")
else:
    print(f"Test 1 failed expected {answer} got {output}")

#Test 2
input = -123
output = solution.reverse(input)
answer = -321
if Test(output, answer):
    print("Test 2  passed")
else:
    print(f"Test 2 failed expected {answer} got {output}")

#Test 3
input = 120
output = solution.reverse(input)
answer = 21
if Test(output, answer):
    print("Test 3  passed")
else:
    print(f"Test 3 failed expected {answer} got {output}")