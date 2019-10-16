import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# print(Queue)
class LRUCache:
	"""
	Our LRUCache class keeps track of the max number of nodes it
	can hold, the current number of nodes it is holding, a doubly-
	linked list that holds the key-value entries in the correct
	order, as well as a storage dict that provides fast access
	to every node stored in the cache.
	"""
	def __init__(self, limit=10):
		self.limit = limit
		self.cache = Queue()
		self.dictionary = {}
		self.length = 0

	"""
	Retrieves the value associated with the given key. Also
	needs to move the key-value pair to the end of the order
	such that the pair is considered most-recently used.
	Returns the value associated with the key or None if the
	key-value pair doesn't exist in the cache.
	"""
	def get(self, key):
		if key in self.dictionary:
			node = self.dictionary[key]
			print(1, node)
			self.cache.storage.move_to_front(node)
			# print('aaa',node.value[key])
			return node.value[key]
		else:
			return None
	
	"""
	Adds the given key-value pair to the cache. The newly-
	added pair should be considered the most-recently used
	entry in the cache. If the cache is already at max capacity
	before this entry is added, then the oldest entry in the
	cache needs to be removed to make room. Additionally, in the
	case that the key already exists in the cache, we simply
	want to overwrite the old value associated with the key with
	the newly-specified value.
	"""
	def set(self, key, value):
		if key in self.dictionary:
			node = self.dictionary[key]
			node.value = {key: value}
			self.cache.storage.move_to_front(node)
		else:
			self.cache.enqueue({ key: value})
			self.length += 1
			if self.length > self.limit:
				removed_item = self.cache.dequeue()
				for dictionary_key in removed_item:
					del self.dictionary[dictionary_key]
			self.dictionary[key] = self.cache.storage.head
			
cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
print(cache.cache, cache.dictionary)
cache.set('item3', 'd')
print(cache.cache, cache.dictionary)
cache.set('item3', 'z')
print(cache.cache, cache.dictionary)

print(cache.get('item2'))


class LectureLRUCache:
	 def __init__(self, limit=10):
		self.limit = limit
		self.order = DoublyLinkedList()
		self.storage = {}
		self.size = 0
	 def get(self, key):
		 if key in self.storage:
			 node = self.storage[key]
			 self.order.move_to_end(node)
			 self.order.move_to_end(node)
			 return node.value[1]
		 else:
			 return None
	   
	 def set(self, key, value):
	   if key in self.storage:
		   node = self.storage[key]
		   node.value = (key, value)
		   self.order.move_to_end(node)
		   return
		if self.size == self.limit:
			del self.storage[self.order.head.value[0]]
			self.order.remove_from_head()
			self.size -= 1
		self.order.add_to_tail((key, value))
		self.storage[key] = self.storage.tail
		self.size += 1