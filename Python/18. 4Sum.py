#Problem Requirements
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


#Design (in Design Folder)
"""
Trying 3Sum solution with an aditional fixed element

Better design and solution at https://leetcode.com/problems/4sum/solutions/737096/sum-megapost-python3-solution-with-a-detailed-explanation/
"""

#Implementation Problems and Solutions
"""
Working 3 Sum with fixed elements at start and end wasn't working, so I jad adjust the fixed pointer for a and b
This is pretty much brute force
"""

#Code Start
from typing import List


class Solution(object):
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        sol = []

        #1 If length < 4 no quad possible
        if(len(nums) < 4):
            return sol
        
        #2 Sort the numbers in ascending order
        nums.sort()

        #3.a Fix first 
        for a in range (len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            #3.b Fix second
            for b in range(a + 1, len(nums)):
                    if b > a + 1 and nums[b] == nums[b-1]:
                        continue
                    # 4 Two pointers
                    c = b + 1
                    d = len(nums) - 1

                    #5 Two Sum
                    while c < d:

                        if nums[a] + nums[b] + nums[c] + nums[d] < target:
                            c += 1
                        elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                            d -= 1
                        else:
                            sol.append([nums[a], nums[b], nums[c], nums[d]])
                            c += 1
                            while nums[c] == nums[c-1] and c < d:
                                c += 1
        return sol


#Test Code
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [1,0,-1,0,-2,2]
target = 0
output = solution.fourSum(input, target)
answer = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Test (1, output, answer) 

#Test 2
input, target = [2,2,2,2,2], 8
output = solution.fourSum(input, target)
answer = [[2,2,2,2]]
Test (2, output, answer) 

#Test 3
input = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
target = 6
output = solution.fourSum(input, target)
answer = []
Test (3, output, answer) 

#Test 4
input = [-3,-1,0,2,4,5]
target = 0
output = solution.fourSum(input, target)
answer = [[-3,-1,0,4]]
Test (4, output, answer) 