""" 2.7 Implement a function to check if a linked list is a palindrome 
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

    def IsPalindrome(self):
        flip = False
        half = self.head
        current = self.head
        firsthalf = []
        secondhalf = []
        while current:
            if (flip):
                data = half.get_data()
                firsthalf.append(data)
                half = half.get_next()
            flip = not flip
            current = current.get_next()
        print("\nFirst half of the list:")
        print(firsthalf)
        half = half.get_next() #Before appending the second list , advance the second list after moving the pointer one step
        while half:
            data = half.get_data()
            secondhalf.append(data)
            half = half.get_next()
        print("\nSecond half of the list:")
        print(secondhalf)
        print("\nReversing Second half of the list ...")
        secondhalf.reverse()
        if firsthalf == secondhalf:
            print("This is a palindrome linked list ...")
        else:
            print("This is not a palindrome linked list ...")

s = LinkedList()
s.insert(31)
s.insert(2)
s.insert(3)
s.insert(7)
s.insert(10)
s.insert(4)
s.insert(5)
s.show()
s.IsPalindrome()

s1 = LinkedList()
s1.insert(0)
s1.insert(1)
s1.insert(2)
s1.insert(1)
s1.insert(0)
s1.show()
s1.IsPalindrome()
