class Node:
    def __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
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
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()
    def findValue(self,value):
        if self.data > value:
            if self.left == None:
                print("value not found")
                return
            self.left.findValue(value)
            return
        elif self.data < value:
            if self.right == None:
                print("value not found")
                return
            self.right.findValue(value)
            return
        else:
            print("value found")
            return

if __name__ == "__main__":

    tree = Node(2)
    tree.insert(5)
    tree.insert(1)
    tree.insert(10)
    tree.insert(4)
    tree.findValue(4)
    tree.findValue(1)
    tree.findValue(6)