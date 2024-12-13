"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #Solution
        """
        For each number in the array  (start at 0 index) record the difference between the target number and the current number in the array and save the number and it's index it in a map. Number is key value is index
        If the difference between the two numbers exist in the map. Return that numbers index in the array and the current numbers index
        
        Ex. 1
        First number 2: 
        Target - number = diff
        9 - 2 = 7
        check is dict contains diff. Fail
        Add 2 to the map with a value of 0
        Second number 7:
        9 - 7 = 2
        Check if dict contains 2. Success
        Return List[dict[2], currentIndex or (i)]
        Return 


        """

        number_map = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in number_map:
                return [number_map[diff], i]
            number_map[nums[i]] = i

test = Solution()

print(test.twoSum([2,7,11,15], 9))
print(test.twoSum([3,2,4], 6))



        

   