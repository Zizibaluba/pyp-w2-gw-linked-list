class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next
    
    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        if self.elem == None and other == None:
            return True
        elif self.elem != None and other == None:
            return False
        elif self.elem == None and other != None:
            return False
        return self.elem == other.elem

    def __repr__(self):
        return self