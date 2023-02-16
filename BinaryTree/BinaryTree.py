
class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrderTraversal(self):
        if self.data is None:
            return
        if self.left:
            self.left.inOrderTraversal()
        print(self.data,end=','),
        if self.right:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        if self.data is None:
            return
        print(self.data,end=',')
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()
        

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.inOrderTraversal()
print()
root.preOrderTraversal()
print()