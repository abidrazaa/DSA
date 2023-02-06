class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def pushAtEnd(self,nodeValue):

        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = newNode
        

            