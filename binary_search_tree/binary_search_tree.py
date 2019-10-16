import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.value}"
    
    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self.value = value
        elif value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        
                
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
       if not self.right:
           return self.value
       else:
           return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        while True:
            if node == None and storage.len() == 0:
                break
            elif node == None:
                node = storage.dequeue()
            else:
                print(node.value)
                storage.enqueue(node.left)
                storage.enqueue(node.right)
                node = storage.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # I missed the iterative part, here it is recursively :(
        # if node == None:
        #     return
        # print(node.value)
        # self.dft_print(node.right)
        # self.dft_print(node.left)
        #*********************************************************#
        storage = Stack()
        while True:
            if node == None and storage.len() == 0:
                break
            elif node == None:
                node = storage.pop().left
            else:
                print(node.value)
                storage.push(node)
                node = node.right
            
                
            
            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)

bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
# # print(bst.left.right.value)
# # print(bst.right.left.value)
# bst.in_order_print(bst)
# bst.dft_print(bst)
bst.bft_print(bst)


# for_each
# def print_nodes(node):
#     print(node)
# bst.for_each(print_nodes)
