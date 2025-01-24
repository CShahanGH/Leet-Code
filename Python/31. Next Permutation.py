#Problem Requirements
"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


#Design
"""
Two pointers
https://www.youtube.com/watch?v=6qXO72FkqwM 
https://www.youtube.com/watch?v=quAS1iydq7U
"""

#Implementation Problems and Solutions
"""
Had to look up how to reverse a sublist in python

Example
# Reverse the sub-list from index 2 to 4 (exclusive)
my_list[2:5] = my_list[2:5][::-1]

"""

#Code Start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ascending_size = 1
        #Find largest ascneding_size from end
        for i in range(len(nums) - 1, 0, -1): 

            if i - 1 >= 0 and nums[i] <= nums[i-1]: 
                ascending_size += 1
                continue

            #Left (i-1) be smaller than right(i)
            
            left = i - 1  #Left Swap Target
            right = i #Right Swap Target

            if ascending_size > 1: #1, 2, 3, [6, 5, 4] size = 3
                #Find swap target to the right of left
                for j in range(len(nums) - 1, left, -1):
                    
                    #Swap target should be the smallest number from ascending_size > nums[left]
                    if nums[j] <= nums[left]:
                        continue

                    right = j
                    break

            #Swap nums[left], nums[right]
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

        
            #Reverse nums from ascending_size
            if ascending_size > 1:
                nums[len(nums) - ascending_size: len(nums)] = nums[len(nums) - ascending_size: len(nums)][::-1]
                print(nums)

            return
        
        #Case all ascending from end reverse array
        nums.reverse()
        return 



#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [1,3,2]
output = solution.nextPermutation(input)
answer = None

Test (1, output, answer) 



