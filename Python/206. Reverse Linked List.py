#Problem Requirements
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


#Design
"""
Use a "temp" or "dummy" for swapping
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: #Iterative

        if head == None or head.next == None:
            return head

        prev = None 
        dummy = ListNode()
        current = head

        while dummy != None:
            dummy = current.next
            if dummy == None:
                head = current
            
            current.next = prev
            prev = current 
            current = dummy
        
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: #Recursive

        def reverse(current, prev):
            
            if current == None:
                return prev
            
            nextNode = current.next
            current.next = prev

            return reverse(nextNode, current)

        return reverse(head, None) 
    
    
    
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
output = solution.reverseList(input)
answer = None




