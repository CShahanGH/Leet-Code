#Problem Requirements
"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""


#Design
"""
Neetcode Dequeue with Sliding Window
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #Return fast
        if k == 1:
            return nums
        
        ans = []
        deck = deque()
        left = right = 0 #Window

        while right < len(nums):

            while deck and nums[deck[-1]] < nums[right]: #Keep deque nums[i0] > nums[i1] > nums[i2]
                deck.pop()
            deck.append(right) 

            if left > deck[0]: #Pop index when no longer in window
                deck.popleft()

            if (right + 1) >= k: #Right starts at 0 that's why + 1
                ans.append(nums[deck[0]])
                left += 1
            right += 1

                    
        return ans



#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
nums = [1,3,-1,-3,5,3,6,7]
k = 3
output = solution.maxSlidingWindow(nums, k)
answer = [3,3,5,5,6,7]

Test (1, output, answer) 



