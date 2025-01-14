#Problem Requirements
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


#Design 
"""
This should be an easy problem using dummy pointers. 

You can also use recursion with a base case to return when list1 and list2 are empty
"""

#Implementation Problems and Solutions
"""
My recursion implementation never worked so credit for this solution goes to nitts:
https://leetcode.com/problems/merge-two-sorted-lists/solutions/6048156/video-using-dummy-pointer-and-recursion-solution-as-a-bonus/

I was over thinking it X_X
"""

#Code Start
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2 #Return the non empty node if 1 of the nodes are empty
        
        
        if list1.val > list2.val:
            list1, list2 = list2, list1 #Python Swap Ensuring List1.val is < or == List2,.val

        list1.next = self.mergeTwoLists(list1.next, list2) #Recursion on list1

        return list1


        
        


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
input1 = ListNode(1, ListNode(2, ListNode(4)))
input2 = ListNode(1, ListNode(3, ListNode(4)))
output = solution.mergeTwoLists(input1, input2)
answer = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
Test (1, output, answer) 



