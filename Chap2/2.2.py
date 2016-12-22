""" 2.2 Implement an algorithm to find the kth to last element of a singly linked list. 
"""
__author__ = 'karsaxen'

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def show(self):
        print("\n Displaying the linked list :-")
        current = self.head
        while current:
            data = current.get_data()
            print(str(data)+"->",end="")
            current = current.get_next()

    #In this approach we maintain two pointers. One moves K position ahead first . Once both are moved together the first one
    #Will be at length - K position.

    def findkelement(self,k):
        anchor = self.head
        follower = self.head
        i=0
        while i < k:
            anchor = anchor.get_next()
            i = i+1
        while anchor:
            anchor = anchor.get_next()
            follower = follower.get_next()
        print("\n Displaying the Kth from last element :-")
        kdata = follower.get_data()
        print(str(kdata))

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

s = LinkedList()
s.insert(31)
s.insert(2)
s.insert(3)
s.insert(7)
s.insert(10)
s.insert(4)
s.show()
s.findkelement(3)
s.findkelement(4)
s.findkelement(1)