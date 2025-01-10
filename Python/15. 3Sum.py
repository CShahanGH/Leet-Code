#Problem Requirements
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

 
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


#Design 
"""
In the design folder as 15.3Sum excalidraw
"""

#Implementation Problems and Solutions
"""
I have this code answer.append(triplet). Triplet is a list of integers triplet = [nums[fix], twosum[0], twosum[1]]
I get error: TypeError: list.append() takes exactly one argument (0 given)
If I try answer.append([triplet[0], triplet[1], triplet[2]]). I get the same error 

Solution
Answer was initalized wrong answer = List[List[int]] -> answer: List[List[int]] = [] Thank you python :)

Testing Dups Error 
for list in answer:
    if set(list) == set(triplet):
        break #Set answer contains triplet
    answer.append(triplet) <- Appendeded duplicate triplets

Solution
dup = False
for list in answer:
    if set(list) == set(triplet):
        dup = True
        break #Set answer contains triplet
if not dup:
    answer.append(triplet)

Problem
Not all triplets are being found. Need a different implementation of TwoSum

Solution -> Redesign. 

Problem
Time Limit Exceeded:
Solution -> Use someone elses design niits -> https://leetcode.com/problems/3sum/solutions/5055810/video-two-pointer-solution/ 

I just needed to skip the same element from one side of the sorted array when a triplet is found
"""

#Code Start
from typing import List


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer: List[List[int]] = [] 

        nums.sort() #Timesort thank you python

        for x in range (0, len(nums)):
            #Skip same elements
            if x > 0 and nums[x] == nums[x-1]:
                continue

            target = -1 * nums[x]
            y = x + 1 #Since we will skip repeating numbers of the left side we can always set y to x + 1
            z = len(nums) - 1
            
            while y < z:
                
                #Move pointers if no match
                if nums[z] + nums[y] > target:
                    z -= 1
                elif nums[z] + nums[y] < target:
                    y += 1
                else:
                    answer.append([nums[x], nums[y], nums[z]])
                    y += 1 
                    #Skip same element 
                    while nums[y] == nums[y-1] and y < z:
                        y += 1

        return answer


#Test Code 
def Test(id, output, answer):
    output == answer
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [-1,0,1,2,-1,-4]
output = solution.threeSum(input)
answer = [[-1,-1,2],[-1,0,1]]
Test (1, output, answer) 


#Test 2
input = [0,1,1]
output = solution.threeSum(input)
answer = []
Test (2, output, answer) 

#Test 3
input = [0,0,0]
output = solution.threeSum(input)
answer = [[0,0,0]]
Test (3, output, answer) 

#Test 4
input = [-2,0,1,1,2]
output = solution.threeSum(input)
answer = [[-2,0,2],[-2,1,1]]
Test (4, output, answer) 

#Test 5
input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
output = solution.threeSum(input)
answer = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
Test (5, output, answer) 

#Test 6
input = [-1,0,1,0]
output = solution.threeSum(input)
answer = [[-1,0,1]]
Test (6, output, answer) 