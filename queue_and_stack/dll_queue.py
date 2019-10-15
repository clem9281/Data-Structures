import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
    def __str__(self):
        return f"Queue: storage: {self.storage}"
        
    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.storage.length is 0:
            return
        old_tail = self.storage.tail
        self.storage.remove_from_tail()
        return old_tail.value

    def len(self):
        return len(self.storage)

# q = Queue()
# q.enqueue(4)
# q.enqueue(3)
# q.enqueue(2)
# q.enqueue(6)
# print(f'"q": {q}')
# print(q.dequeue())
# print(f'"q": {q}')
# print(q.dequeue())
# print(f'"q": {q}')
# print(q.dequeue())
# print(f'"q": {q}')
# print(q.dequeue())
# print(f'"q": {q}')