import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
    
    def __str__(self):
        return f"Stack: storage: {self.storage}"
    
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size is 0:
            return
        old_tail = self.storage.tail
        self.storage.remove_from_tail()
        self.size -= 1
        return old_tail.value

    def len(self):
        return self.size

s = Stack()
s.push(4)
s.push(3)
s.push(2)
s.push(6)
print(f'"s": {s}')
print(s.pop())
print(f'"s": {s}')
print(s.pop())
print(f'"s": {s}')
print(s.pop())
print(f'"s": {s}')
print(s.pop())
print(f'"s": {s}')