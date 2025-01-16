#Problem Requirements
"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""


#Design (in Design)
"""

"""

#Implementation Problems and Solutions
"""
Needed to track previous node to connect list and once again work on recursion
Beautfiful recursive solution in c++
https://leetcode.com/problems/swap-nodes-in-pairs/

"""

#Code Start
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if not head or not head.next:
            return head
        
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head

        return temp


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    while answer != None:
        try:
            assert output.val == answer.val
        except:
            print(f"Test {id} failed got {output.val} expected {answer.val}")
        answer = answer.next
        output = output.next
    print(f"Test {id} passed")


solution = Solution()

#Test 1

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
output = solution.swapPairs(input)
answer = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))

Test (1, output, answer) 



