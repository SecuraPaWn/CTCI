"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    ptr1 = headA
    while(ptr1 is not None):
        ptr2 = headB
        while(ptr2 is not None):
            if(ptr1.data == ptr2.data):
                return ptr1.data
            ptr2 = ptr2.next
        ptr1 = ptr1.next
        
  
  
