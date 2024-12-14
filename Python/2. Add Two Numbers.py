"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

#Implementation
"""
Each node is in it's respective place of the decimal system. Meaning none 1 is in the one's place, node two is in the two's place, node 3 is in the 100s place (4, 1000, 5, 10000 etc)
So for each node. Sum = 0. Then traverse each node and multiply the number by it's spot in the decimal system (1 is 1, 2 is 10, 3, is 100) and add it to sum. Then add all sums together. 
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3_list = []
        #Find Sum1
        sum1 = 0
        decimal = 1
        
        #Traverse nodes until the current node doesn't have a next node
        while True:
            sum1 += l1.val * decimal

            l1 = l1.next
            decimal *= 10

            if l1 == None:
                break

        #Find Sum2
        sum2 = 0
        decimal = 1
        while True:
            sum2 += l2.val * decimal

            l2 = l2.next
            decimal *= 10

            if l2 == None:
                break
        
        sum1_sum2 = sum1 + sum2

        #Convert the sum into a string
        str_sum1_sum2 = str(sum1_sum2)
        #Count backwards 
        for i in range (len(str_sum1_sum2), 0, -1):
            #Convert each string to an int 
            val = int(str_sum1_sum2[i-1])
            #Store Return List Values
            l3_list.append(val)
        
        #Make Return Linked List
        l3 = l3tail = ListNode(l3_list[0])
        for x in range(1, len(l3_list)):
            l3tail.next = ListNode(l3_list[x])
            l3tail = l3tail.next
        
        return l3

        
"""Test Code"""
    
        
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

          
test = Solution()
l3 = test.addTwoNumbers(l1, l2)
while True:
    print(l3.val)
    l3 = l3.next

    if l3 == None:
        break
