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