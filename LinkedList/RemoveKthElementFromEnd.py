class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# ACTUAL IMPLEMENTATION IN LinkedList file

def removeKthNodeFromEnd(head, k):
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