import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        self.length = 0
    def __str__(self):
        return f"Queue: storage: {self.storage}"
        
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.length += 1
        # pass

    def dequeue(self):
        if self.length is 0:
            return
        old_head = self.storage.head
        self.storage.remove_from_head()
        self.length -= 1
        return old_head.value

    def len(self):
        return self.length

q = Queue()
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(6)
print(f'"q": {q}')
print(q.dequeue())
print(f'"q": {q}')
print(q.dequeue())
print(f'"q": {q}')
print(q.dequeue())
print(f'"q": {q}')
print(q.dequeue())
print(f'"q": {q}')