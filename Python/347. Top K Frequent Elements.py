#Problem Requirements
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


#Design 
"""
Hash_map (dict) counting elements
List storing lists of the elements at an index count
"""

#Implementation Problems and Solutions
"""
Credit to neetcode
"""

#Code Start
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ele_count = {}
        bucket = [[] for i in range( len(nums) + 1)] #Frequency
        result = []

        #Count Elements
        for n in nums:
            ele_count[n] = ele_count.get(n, 0) + 1

        #Add elements to 'buckets' where index in the count of the elements
        for ele, count in ele_count.items():
            bucket[count].append(ele)
        
        #Traverse backwards in backwards because higher element counts are on the end
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result



#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = None
output = None
answer = None

Test (1, output, answer) 



