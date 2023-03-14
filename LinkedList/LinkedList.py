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

    def removeKthNodeFromEnd(self, head, k):
        # We will be doing this by two pointer approach
        first = head
        second = head
        counter = 0

        # we are moving second pointer k nodes ahead of the first
        while counter<k:
            second = second.next
            counter+=1

        # now we have second pointer k nodes ahead of the first. If the second
        # pointer points to NULL, this means we have to remove the head node
        # else, we will increment both the pointer until the second pointer reaches the NULL 
        # so we'll have our first pointer k nodes before the end :))

        if second is None:
            # removing the head node
            head.value = head.next.value
            head.next = head.next.next
        
            return

        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next
    
    def removeDuplicatesFromLinkedList(self,linkedList):
        # We are using two pointers approach
        first = linkedList
        second = linkedList.next

        while second is not None:
            if first.data == second.data:
                first.next = second.next
            else:
                first = second
            second = second.next


linkedList = LinkedList()

linkedList.pushAtBeginning('1')
linkedList.pushAtBeginning('2')
linkedList.pushAtBeginning('3')
linkedList.pushAtBeginning('3')
linkedList.pushAtBeginning('3')
linkedList.pushAtBeginning('4')
linkedList.pushAtBeginning('5')

print("Original Linked List")
linkedList.printLinkedList()
print()

linkedList.removeDuplicatesFromLinkedList(linkedList.head)
print("Remove Duplicates From Linked List:")
linkedList.printLinkedList()
print()

linkedList.removeKthNodeFromEnd(linkedList.head,3)
print('Remove Kth Element from end:')
linkedList.printLinkedList()
print()

linkedList.insertAfter('inserted',linkedList.head.next)
linkedList.pushAtEnd('end') 
# linkedList.printLinkedList()
linkedList.reverseLinkedList()
print('Reverse Linked List:')
linkedList.printLinkedList()
print(linkedList.searchInLinkedList('202'))
linkedList.deleteNodeAtGivenPosition(1)
print()
linkedList.printLinkedList()
print()


