#Problem Requirements
"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


#Design
"""
Binary search on 0th column to narrow down row 
Another binary search on target row to find eleement
"""

#Implementation Problems and Solutions
"""
A comma in my test input almost made me lose my mind
"""

#Code Start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1

        while left <= right:

            row = left + (right - left) // 2

            if matrix[row][0] <= target and matrix[row][-1] >= target: #Row found

                #Binary search on row
                left = 0
                right = len(matrix[row]) - 1

                while left <= right:

                    col = left + (right - left) // 2

                    if matrix[row][col] == target:
                        return True
                    
                    if matrix[row][col] < target: #Move To Right
                        left = col + 1
                    else:
                        right = col - 1
                
                return False

            if matrix[row][0] > target: #Move down
                right = row - 1
            else: #Row end < target
                left = row + 1
        
        return False




#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [[1,3,5,7],
         [10,11,16,20],
         [23,30,34,60]]
output = solution.searchMatrix(input, 3)
answer = True
Test(1, output, answer)

#Test 2
input = [[1,3,5]]
output = solution.searchMatrix(input, 4)
answer = False 
Test(2, output, answer)



