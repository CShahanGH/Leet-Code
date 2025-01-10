#Problem Requirements
"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


#Design
"""
Very similar to 15. 3Sum. We have a target, and we can add 1 and subtract 1 from the target until a valid 3sum is found.

Use the absolute value to determine the distance between the target and two other numbers on the number line (also in design folder)
"""

#Implementation Problems and Solutions
"""
I wish recursion was fast

Solution don't use recursion
"""

#Code Start
from typing import List

class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort() #Timesort thank you python

        sum = nums[0] + nums[1] + nums[2] #default start

        for x in range (0, len(nums)):
            #Skip same elements
            if x > 0 and nums[x] == nums[x-1]:
                continue

            y = x + 1 #Since we will skip repeating numbers of the left side we can always set y to x + 1
            z = len(nums) - 1
            
            while y < z:
                
                newsum = nums[x] + nums[y] + nums[z]
                
                if newsum == target:
                    return target
                #Update sum that's closest to target
                if abs(sum - target) > abs(newsum - target):
                    sum = newsum

                if newsum > target:
                    z -= 1
                elif newsum < target:
                    y += 1
                
        return sum




#Test Code
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input =  [-1,2,1,-4]
target = 1
output = solution.threeSumClosest(input, target)
answer = 2
Test (1, output, answer) 

#Test 2
input =  [0, 0, 0]
target = 1
output = solution.threeSumClosest(input, target)
answer = 0
Test (2, output, answer) 
