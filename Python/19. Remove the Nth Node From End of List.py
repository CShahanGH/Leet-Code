#Problem Requirements
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""


#Design (In Design Folder)
"""
Traverse the list and keep track of the nth - 1 node.
"""

#Implementation Problems and Solutions
"""
Had to fix case when n was still greater than 0, and had to handle removing tail and head cases
"""

#Code Start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        #Traverse the List Until Empty
        current = nNode = head

        while current.next != None:
                
            current = current.next
            
            if n - 1 < 0:
                nNode = nNode.next
            else:
                n -= 1
        
        if n > 0 and nNode == head: #Remove head
            head = head.next
        elif nNode.next == current: #Remove Tail
            nNode.next = None
        else:
            nNode.next = nNode.next.next

        return head



#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output : ListNode, answer : ListNode):
    while output != None:
        try:
            assert output.val == answer.val
        except:
            print(f"Test {id} failed got {output.val} expected {answer.val}")
        output = output.next
        answer = answer.next
    print(f"Test {id} passed")

solution = Solution()

#Test 1
n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
n5 = ListNode(5)
n4.next = n5

input, n = n1, 2
output = solution.removeNthFromEnd(n1, n)
answer = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))

Test (1, output, answer) 

#Test 2
n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2

input, n = n1, 1
output = solution.removeNthFromEnd(n1, n)
answer = ListNode(1)
Test (2, output, answer) 