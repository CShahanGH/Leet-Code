#Problem Requirements
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""


#Design (in Design Folder)
"""

"""

#Implementation Problems and Solutions
"""
Implemenation by Code in Motion merge sort
"""

#Code Start
from typing import List, Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        while len(lists) != 1:
            sorted = []
            for i in range (0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                sorted.append(self.mergeTwoLists(list1, list2))
            lists = sorted

        return lists[0]



    #Leetcode 21
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
input = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
output = solution.mergeKLists(input)
answer = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))

Test (1, output, answer) 



