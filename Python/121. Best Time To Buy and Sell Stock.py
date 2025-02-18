#Problem Requirements
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


#Design
"""
Sliding Window
"""

#Implementation Problems and Solutions
"""
I think I over complicated the problem, but it works
"""

#Code Start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        k = 2 #Starting window size
        Max = max(prices[-k:]) #Start max of last 2 elements in list
        maxprofit = 0

        while k <= len(prices):

            l = -k #Expand window backwards

            if prices[l] < Max: #Money                 
                profit = Max - prices[l]
                maxprofit = max(profit, maxprofit)
            else:
                Max = prices[l]
            k += 1
        
        return maxprofit

#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = [4,7,1,2]
output = solution.maxProfit(input)
answer = 3

Test (1, output, answer) 



