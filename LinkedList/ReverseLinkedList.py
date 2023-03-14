# https://www.geeksforgeeks.org/reverse-a-linked-list/ to see diagramtic flow

# ACTUAL IMPLEMENTATION IN LinkedList file

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