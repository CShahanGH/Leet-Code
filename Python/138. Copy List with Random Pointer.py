#Problem Requirements
"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""


#Design
"""
Use a list storing old nodes and new nodes 

Might revisit later and solve without using other data structures to minimize memory and solve in one pass
"""

#Implementation Problems and Solutions
"""

"""

#Code Start
from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #Fail
        if not head:
            return
        
        old_nodes: List[Node] = []
        new_nodes: List[Node] = []

        #Create lists
        while head:
            old_nodes.append(head)
            node = Node(head.val) #Set value
            new_nodes.append(node)
            head = head.next

        #Set pointers
        for i in range(len(new_nodes)):

            #Next
            if i + 1 < len(new_nodes):
                new_nodes[i].next = new_nodes[i+1]
            
            #Random 
            if old_nodes[i].random:

                index = old_nodes.index(old_nodes[i].random)
                new_nodes[i].random = new_nodes[index]
        
        #Return head of new_nodes
        return new_nodes[0]
        



        




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



