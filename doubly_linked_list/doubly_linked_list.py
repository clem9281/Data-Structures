"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
	def __init__(self, value, prev=None, next=None):
		self.value = value
		self.prev = prev
		self.next = next
	def __str__(self):
		return f"ListNode: {self.value}"

	"""Wrap the given value in a ListNode and insert it
	after this node. Note that this node could already
	have a next node it is point to."""
	def insert_after(self, value):
		current_next = self.next
		self.next = ListNode(value, self, current_next)
		if current_next:
			current_next.prev = self.next

	"""Wrap the given value in a ListNode and insert it
	before this node. Note that this node could already
	have a previous node it is point to."""
	def insert_before(self, value):
		current_prev = self.prev
		self.prev = ListNode(value, current_prev, self)
		if current_prev:
			current_prev.next = self.prev

	"""Rearranges this ListNode's previous and next pointers
	accordingly, effectively deleting this ListNode."""
	def delete(self):
		if self.prev:
			self.prev.next = self.next
		if self.next:
			self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
	def __init__(self, node=None):
		self.head = node
		self.tail = node
		self.length = 1 if node is not None else 0

	def __str__(self):
		current_node = self.head
		values = ""
		while current_node:
			if current_node is self.tail:
				values += str(current_node.value)
			else:
				values += str(current_node.value) + ", " 
			current_node = current_node.next
		return f'DoublyLinkedList: values: [{values}], length: {self.length}'

	def __len__(self):
		return self.length

	"""Wraps the given value in a ListNode and inserts it 
	as the new head of the list. Don't forget to handle 
	the old head node's previous pointer accordingly."""
	def add_to_head(self, value):
		new_head = ListNode(value, None, None)
		if not self.head and not self.tail:
			self.head = new_head
			self.tail = new_head
		else:
			new_head.next = self.head
			self.head.prev = new_head
			self.head = new_head
		self.length += 1

	"""Removes the List's current head node, making the
	current head's next node the new head of the List.
	Returns the value of the removed Node."""
	def remove_from_head(self):
		old_head_value = self.head.value
		self.delete(self.head)
		return old_head_value

	"""Wraps the given value in a ListNode and inserts it 
	as the new tail of the list. Don't forget to handle 
	the old tail node's next pointer accordingly."""

	def add_to_tail(self, value):
		new_tail = ListNode(value, None, None)
		if not self.head and not self.tail:
			self.head = new_tail
			self.tail = new_tail
		else:
			new_tail.prev = self.tail
			self.tail.next = new_tail
			self.tail = new_tail
		self.length += 1

	"""Removes the List's current tail node, making the 
	current tail's previous node the new tail of the List.
	Returns the value of the removed Node."""
	def remove_from_tail(self):
		old_tail_value = self.tail.value
		self.delete(self.tail)
		return old_tail_value

	"""Removes the input node from its current spot in the 
	List and inserts it as the new head node of the List."""
	def move_to_front(self, node):
		if node is self.head:
			return
		value = node.value
		self.delete(node)
		self.add_to_head(value)
			

	"""Removes the input node from its current spot in the 
	List and inserts it as the new tail node of the List."""
	def move_to_end(self, node):
		if node is self.tail:
			return
		value = node.value
		self.delete(node)
		self.add_to_tail(value)

	"""Removes a node from the list and handles cases where
	the node was the head or the tail"""
	def delete(self, node):
		if node is self.head and node is self.tail:
			self.head = None
			self.tail = None
		elif node is self.head:
			self.head = node.next
			node.delete()
		elif node is self.tail:
			self.tail = node.prev
			node.delete()
		else:
			node.delete()
		self.length -= 1
			
		
	"""Returns the highest value currently in the list"""
	def get_max(self):
		if not self.head and not self.tail:
			return None
		largest = self.head.value
		current_node = self.head
		while current_node:
			if current_node.value > largest:
				largest = current_node.value
			current_node = current_node.next
		return largest


# dll = DoublyLinkedList(ListNode(1))
# print(dll)