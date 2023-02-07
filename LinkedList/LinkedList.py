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

    def pushAtBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self,data,prev):
        newNode = Node(data)
        newNode.next = prev.next
        prev.next = newNode

    def printLinkedList(self):
        init = self.head
        while init is not None:
            print(init.data,end=" -> ")
            init = init.next
    
    def searchInLinkedList(self,target):
        curr = self.head

        while curr is not None:
            if curr.data == target:
                return True

            curr = curr.next

        return False
    
    def deleteNodeAtGivenPosition(self,position):
        curr = self.head
        prev = None
        counter = 0
        while curr is not None:
            if position == 0:
                self.head = self.head.next
                return
            elif counter == position:
                prev.next = curr.next
                return
            counter+=1
            prev = curr
            curr = curr.next



    # https://www.geeksforgeeks.org/reverse-a-linked-list/ to see diagramtic flow

    def reverseLinkedList(self):
        # To set first node's next as null/None 
        prev = None
        curr = self.head

        # iterating over the list and just changing the direction of pointer in opposite direction
        while curr is not None:
            # saving the very next node to be manipulated because in the next lines curr.next will be edited
            next = curr.next
            # setting current node's next as the previous node (changing the pointer direction)
            curr.next = prev
            # setting previous node as current node for the next node
            prev = curr
            # setting the current node to the next node as we move forward in the list
            curr = next
        
        # setting linked list head to the last node
        self.head = prev



linkedList = LinkedList()

linkedList.pushAtBeginning('1')
linkedList.pushAtBeginning('2')
linkedList.pushAtBeginning('3')
linkedList.insertAfter('inserted',linkedList.head.next)
linkedList.pushAtEnd('end') 
linkedList.printLinkedList()
linkedList.reverseLinkedList()
linkedList.printLinkedList()
print(linkedList.searchInLinkedList('202'))
linkedList.deleteNodeAtGivenPosition(1)
print()
linkedList.printLinkedList()
print()

