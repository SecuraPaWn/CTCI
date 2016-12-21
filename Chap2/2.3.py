""" 2.3 Implement an algorithm to delete a node in the middle of the singly linked list, given only access to that node.
Input : the node c from the linked list a->b->c->d->e
Result : nothing is returned, but the new linked list looks like a->b->d->e
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

    def find_middle(self):
        flip = False
        half = self.head
        current = self.head
        while current:
            current = current.get_next()
            if (flip):
                half = half.get_next()
            flip = not flip
        print("\n Middle node is %s" % str(half.get_data()))

s = LinkedList()
s.insert(31)
s.insert(2)
s.insert(3)
s.insert(7)
s.insert(10)
s.insert(4)
s.show()
s.find_middle()