#Problem Requirements
"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""


#Design
"""
Binary Search to find slowest eating speed
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #Ex 1
        low = 1 
        high = max(piles)
        k = high 

        while low <= high: #end 4 <= 3

            mid = (low + high) // 2 #6 #3 #4
            
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid) #mid = 6 1 + 1 + 2 + 2 = 6 #mid = 3 1 + 2 + 3 + 4 = 10
            
            if time <= h: #6 #10 # 8
                k = mid #6 #4
                high = mid - 1 #5 #3
            else:
                low = mid + 1 #4

        return k




#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [3,6,7,11]
output = solution.minEatingSpeed(input, 8)
answer = 4

Test (1, output, answer) 



