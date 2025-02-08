#Problem Requirements
"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""


#Design
"""
Binary Search to find right most index, and then two pointer approach target
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Quick find
        if len(numbers) == 2:
            return [1, 2]
        
        left = 0
        right = len(numbers) - 1
        if numbers[len(numbers)//2] > target: #Change starting right index

            #Start binary search
            btarget = target - numbers[0]
            low = 0
            high = len(numbers) - 1

            while low < high:  
                mid = low + (high - low)//2
                
                if numbers[mid] < btarget:
                    #Check right
                    low = mid + 1

                else: #num[mid] > target
                    high = mid - 1
            
            right = high
        
        
        #Two pointer
        if right <= 0:
                right = 1
        while left < right:
            
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left+1, right+1]
            
            if sum < target: #Move left
                left+=1
            else:
                right-=1


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
output = solution.twoSum(input, -2)
answer = [1, 2]

#Test 2
input = [2,7,11,15]
output = solution.twoSum(input, 9)
answer = [1,2]

Test (1, output, answer) 



