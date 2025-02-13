#Problem Requirements
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


#Design
"""
My originally designed partially worked, but I was missing an important part of the problem
"""

#Implementation Problems and Solutions
"""
Shoutout Neetcode
"""

#Code Start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        l, r = 0, len(height)-1
        maxl, maxr = height[l], height[r]

        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                water += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                water += maxr - height[r]

        return water 




            




#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = solution.trap(input)
answer = 6
Test (1, output, answer) 

#Test 2
input = [4,2,0,3,2,5]
output = solution.trap(input)
answer = 9
Test (2, output, answer) 



