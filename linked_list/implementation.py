from .node import Node
from .interface import AbstractLinkedList
from copy import deepcopy

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements == None:
            elements = []
        self.length = len(elements) #index for __iter__ (remember to change this if appending or popping)
        self.start = Node()
        self.end = Node()
        
        if len(elements) == 0:
            self.start = self.end
        elif len(elements) == 1:
            # Build a single node here
            if isinstance(elements, list):
                newnode = Node(elements[0])
                self.start = newnode
                self.end = newnode
            else:
                newnode = Node(elements)
                self.start = newnode
                self.end = newnode
        elif len(elements) > 1:
            # Test For loop to initialize nodes
            self.start = Node(elements[0])
            current_node = self.start
            for item in elements[1:-1]:
                next_node = Node(item)
                current_node.next = next_node
                current_node = next_node
            self.end = Node(elements[-1])
            current_node.next = self.end
        self.cur_pointer = self.start
                
    def __str__(self):
        result = []
        if self.start == None:
            return "[]"
        cur = self.start
        while cur != None:
            result.append(cur.elem)
            cur = cur.next
        return str([(i) for i in result])

    def __len__(self):
        length = 0
        for item in self:
            length += 1
        return length
        

    # iter generator, uses a local variable so iteration can be used multiple times 
    def __iter__(self):
        generator_pointer = self.cur_pointer
        while generator_pointer != None:
            yield generator_pointer.elem
            generator_pointer = generator_pointer.next

    def node_generator(self):
        generator_pointer = self.cur_pointer
        while generator_pointer != None:
            yield generator_pointer
            generator_pointer = generator_pointer.next

    def __getitem__(self, index):
        for node_index, element in enumerate(self):
            if node_index == index:
                return element

    # Needs to abstract self
    def __add__(self, other):
        # Check whether self is an empty LL
        # Check whether other is an empty LL
        # If either are empty, use the other in place of the other
        # If both are occupied, point self.end.next to other.start
       
        # If neither is occupied node, return an empty node
        if self.start.elem == None and other.start.elem == None:
            return self
        
        # Get a copy of self so value by reference doesn't overwrite the original value
        addition_self = deepcopy(self)
        addition_other = deepcopy(other)
        
        if self.start == self.end and self.start.elem == None:
            addition_self.start = other.start
            addition_self.end = other.end
            addition_self.cur_pointer = addition_self.start
        elif other.start == other.end and other.start.elem == None:
            addition_other.start = self.start
            addition_other.end = self.end
            addition_other.cur_pointer = addition_other.start
            return addition_other
        elif len(self) == 1:
            addition_self.start.next = other.start
            addition_self.end = other.end
        elif len(self) > 1:
            addition_self.end.next = other.start
            addition_self.end = other.end
        else:
            raise IndexError
        return addition_self
    
    def __iadd__(self, other):
        # Both LLs are empty, return an empty LL
        if self.start.elem == None and other.start.elem == None:
            return self
        # Check if self is an empty LL
        elif self.start == self.end and self.start.elem == None:
            self.start = other.start
            self.end = other.end
            self.cur_pointer = self.start #Needed because start is at other.start now
            return self
        # Check if other is an empty LL
        elif other.start == other.end and other.start.elem == None:
            return self
        else:
            self.end.next = other.start
            self.end = other.end
            return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for index, item in enumerate(self):
            if item != other[index]:
                return False
        return True

    def __ne__(self, other):
        if len(self) != len(other):
            return True
        for index, item in enumerate(self):
            if item != other[index]:
                return True
        return False
            
    def append(self, elem):
        if isinstance(elem, list):
            elem = LinkedList(elem)
        else:
            elem = LinkedList([elem])
        self += elem
        return self

        # if self.start == Node():
        #     newNode = Node(elem)
        #     self.start = newNode
        #     self.end = newNode
        # else:
        #     newNode = Node(elem)
        #     self.end.next = newNode
        #     self.end = newNode

    def count(self):
        if self.start.elem == None:
            return 0
        count = 0
        cur = self.start
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def pop(self, index=None):
        # Exceptions
        if index > len(self) - 1:
            raise IndexError
        if self.start.elem == None:
            raise IndexError
            
        if index == None:
                index = len(self) - 1
                
        if index == 0:
            pop_value = self[index]
            self.start = self.start.next
            self.cur_pointer = self.start
            return pop_value
        else:
            current_index = 0
            current_node = self.start
            pop_value = 0
            while current_index < index:
                if current_index == index -1:
                    previous_node = current_node
                    pop_value = current_node.next.elem
                    previous_node.next = current_node.next.next
                    break
                current_node = current_node.next
                current_index += 1
            return pop_value
            
        
        # if self.start.elem == None:
        #     raise IndexError()
        # elif self.start.next == None:
        #     new = Node()
        #     result = self.start.elem
        #     self.start = new
        #     self.end = new
        #     return result
        # elif index == None:
        #     cur = self.start
        #     print('cur=',cur.elem)
        #     while cur.next.next != None:
        #         cur = cur.next
        #     result = cur.next
        #     cur.next = None
        #     self.end = cur
        #     return result.elem
        # elif index == 0:
        #     result = self.start.elem
        #     if self.start.next == None:
        #         self.start = None
        #         self.end = None
        #         return result
        #     else:
        #         self.start = self.start.next
        #         return result
        # else:
        #     pre = Node(0)
        #     pre.next = self.start
        #     cur_index = 0
        #     cur = self.start
        #     while cur_index < index:
        #         pre = pre.next
        #         cur = cur.next
        #         cur_index += 1
        #     result = cur.elem
        #     pre.next = cur.next
        #     return result
            