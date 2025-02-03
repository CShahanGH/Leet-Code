#Problem Requirements
"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


#Design
"""
stack storing index of temperature 
"""

#Implementation Problems and Solutions
"""
Had an ungly inner for loop at first looping through all temp indexes in stack
"""

#Code Start
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [0]
        answer = [0 for _ in temperatures]

        for temp_index in range(1, len(temperatures)):
            
            while stack and temperatures[temp_index] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = temp_index - index

            stack.append(temp_index) #Add temp index to stack
        
        return answer


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [73,74,75,71,69,72,76,73]
output = solution.dailyTemperatures(input)
answer = [1,1,4,2,1,1,0,0]

Test (1, output, answer) 




