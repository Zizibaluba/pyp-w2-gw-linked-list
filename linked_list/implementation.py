from .node import Node
from .interface import AbstractLinkedList


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
        
        if len(elements) == 1:
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
        cur = self.start
        while cur != None:
            result.append(cur.elem)
            cur = cur.next
            
        return str([(i) for i in result])

    def __len__(self):
        if self.start == None:
            return 0
        count = 0
        cur = self.start
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    # iter generator, uses a local variable so iteration can be used multiple times 
    def __iter__(self):
        generator_pointer = self.cur_pointer
        while generator_pointer != None:
            yield generator_pointer.elem
            generator_pointer = generator_pointer.next


# from linked_list.implementation import LinkedList
# from linked_list.node import Node
# from linked_list.interface import AbstractLinkedList
# l = LinkedList([1,2,3,4,5])

    def __getitem__(self, index):
        for idx, node in self:
            if idx == index:
                return node

    def __add__(self, other):
        self.end.next = other.start
        self.end = other.end
        return self
        
    def __iadd__(self, other):
        self.end.next = other.start
        self.end = other.end
        return self
        # self.element += other.element
        # return self

    def __eq__(self, other):
        a_val = []
        a = self.start
        while a:
            a_val.append(a.elem)
            a = a.next
        
        b_val = []
        b = other.start
        while b:
            b_val.append(b.elem)
            b = b.next
        #print('a=',a_val,'b=',b_val)
        a = [str(i) for i in a_val]
        b = [str(i) for i in b_val]
        return a == b
    
    # Can probably be implemented the same way as above, except != return statement
    def __ne__(self, other):
        pass
        
    def append(self, elem):
        if elem == None:
            return
        elif self.start == None:
            newNode = Node(elem)
            self.start = newNode
            self.end = newNode
 
        else:
            newNode = Node(elem)
            self.end.next = newNode
            self.end = newNode


    def count(self):
        if self.start == None:
            return 0
        count = 0
        cur = self.start
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def pop(self, index=None):
        if self.start == None:
            raise IndexError()
        if self.start.next == None:
            self.start = None
            self.end = None
        if index == None:
            cur = self.start
            while cur.next.next != None:
                cur = cur.next
            result = cur.next
            cur.next = None
            self.end = cur
            return result.elem
        elif index == 0:
            result = self.start.elem
            if self.start.next == None:
                self.start = None
                self.end = None
                return result
            else:
                self.start = self.start.next
                return result
        else:
            pre = Node(0)
            pre.next = self.start
            cur_index = 0
            cur = self.start
            while cur_index < index:
                pre = pre.next
                cur = cur.next
                cur_index += 1
            result = cur.elem
            pre.next = cur.next
            return result