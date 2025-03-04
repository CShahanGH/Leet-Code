#Problem Requirements
"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""


#Design
"""
Locate tail and using a hash_map to store previous nodes then use a temp node for swapping

Fast and slow pointer from neetcode
"""

#Implementation Problems and Solutions
"""
Too much memory usage from dictionary 
"""

#Code Start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Middle
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        #Reverse
        second = slow.next
        prev = slow.next = None
        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #Merge
        first, second = head, prev
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

            







        


            


#Test Code - sometimes needs to change depending on the data type or constraints of output and answer
def Test(id, output, answer):
    try:
        assert output == answer
        print(f"Test {id} passed")
    except:
        print(f"Test {id} failed got {output} expected {answer}")


solution = Solution()

#Test 1
input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
output = solution.reorderList(input)
answer = None

Test (1, output, answer) 



