#Problem Requirements
"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""


#Design (in Design Folder)
"""

"""

#Implementation Problems and Solutions
"""
I need to refresh linked lists bc this was a disaster without neetcode
"""

#Code Start
from typing import Optional


class ListNode:     
    def __init__(self, val=0, next=None):         
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        last_tail = dummy

        while True: 
            kth = self.getKth(last_tail, k)
            if not kth:
                break
            next_head = kth.next

            #Reverse 
            prev = kth.next
            curr = last_tail.next

            while curr != next_head:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = last_tail.next
            last_tail.next = kth
            last_tail = temp
        
        return dummy.next


        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr



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
input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
output = solution.reverseKGroup(input, k)
answer = ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))

Test (1, output, answer) 



