class node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None
    
    def push(self,new_node_data):
        new_node = node(new_node_data)
        new_node.next = self.head
        self.head = new_node
    
    def printL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def delete(self,position):
        i=0
        current = self.head
        while i<position:
            if current.next == None:
                return 
            current = current.next
            i+=1
        if current.next == None:
            current = None
            return
        new_next = current.next
        current = new_next

if __name__ == "__main__":
    llist = linkedList() 
    llist.push(7) 
    llist.push(1) 
    llist.push(3) 
    llist.push(2) 
    llist.push(8) 
  
    print("Created Linked List: ")
    llist.printL() 
    llist.delete(4) 
    print ("\nLinked List after Deletion at position 4: ")
    llist.printL()
