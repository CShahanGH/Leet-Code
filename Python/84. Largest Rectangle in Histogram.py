#Problem Requirements
"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""


#Design
"""
Use a stack to build rectangles by comparing height of neighboring rectangles - to slow
"""

#Implementation Problems and Solutions
"""
Credit Neetcode
"""

#Code Start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # pair: (index, height)
        maxArea = 0 

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
    
        return maxArea


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [2,1,5,6,2,3]
output = solution.largestRectangleArea(input)
answer = 10

Test (1, output, answer) 



