"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import SinglyLinkedList
import sys
sys.path.append('../singly_linked_list/')


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)
#         return

#     def pop(self):
#         self.size = len(self.storage)
#         if self.size > 0:
#             item = self.storage[self.size-1]
#             self.storage.pop(self.size-1)
#             self.size -= 1
#             return item
#         else:
#             return None


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = SinglyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        self.size = len(self.storage)
        if self.size > 0:
            item = self.storage.remove_last()
            self.size -= 1
            return item
        else:
            None
