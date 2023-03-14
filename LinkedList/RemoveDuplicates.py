class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# sample input ==> 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
# sample output ==> 1 -> 3 -> 4 -> 5 -> 6


# ACTUAL IMPLEMENTATION IN LinkedList file

def removeDuplicatesFromLinkedList(linkedList):
    # We are using two pointers approach
    first = linkedList
    second = linkedList.next

    while second is not None:
        if first.value == second.value:
            first.next = second.next
        else:
            first = second
        second = second.next
    return linkedList