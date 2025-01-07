#Problem Requirements
"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Image -> https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


#Design 
"""
Use two pointers starting at both ends and move the smaller of the two pointers until the right pointer reaches the end. 
"""

#Start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Starting index pointers
        l = 0
        r = len(height) - 1 #Size is guaranted to atleast be 2 in problem
        
        maxWater = 0
        while l < r: #Apporach the midpoint 

            #Calculate Area while l and r are still in bounds
            width = r - l 
            minHeight = min(height[l], height[r])
            water = width * minHeight
            maxWater = max(maxWater, water)

            if height[l] < height [r]: #Nove l and r
                l += 1
            else: #Move r
                r -= 1
            

        return maxWater




#Test Code
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [1,8,6,2,5,4,8,3,7]
output = solution.maxArea(input)
answer = 49

Test (1, output, answer) 

#Test 2 
input = [1, 1]
output = solution.maxArea(input)
answer = 1

Test (2, output, answer) 

#Test 3 
input = [1, 2, 3, 4, 5]
output = solution.maxArea(input)
answer = 6

Test (3, output, answer) 

#Test 4 
input = [5, 4, 3, 2, 1]
output = solution.maxArea(input)
answer = 6

Test (4, output, answer) 

#test 5
input = [1, 1, 1, 20, 20, 1, 1, 1]
output = solution.maxArea(input)
answer = 20

Test (5, output, answer) 


