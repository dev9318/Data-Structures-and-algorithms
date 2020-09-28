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

    def length(self):
        i = 0
        temp = self.head
        while(temp):
            temp = temp.next
            i+=1
        return i           
    
    def search(self,x):
        current = self.head
        while not current == None:
            if(x == current.data):
                return True
            current = current.next
        return False

    def nthnode(self,n,llist):
        llist.nthelement(self.head,n,llist)

    def nthelement(self,curr,n,llist):
        if(curr):    
            if(n==0):
                print(curr.data)
            else:
                llist.nthelement(curr.next,n-1,llist)
        else:
            print("doesn't exist")

    def delete(self,position):
        i=0
        if position == 0:
            self.head = None
        current = self.head
        while i<position-1:
            if current.next == None:
                return 
            current = current.next
            i+=1
        if current.next == None:
            return
        new_next = current.next.next
        current.next = new_next


if __name__ == "__main__":
    llist = linkedList() 
    llist.push(7) 
    llist.push(1) 
    llist.push(3) 
    llist.push(2) 
    llist.push(8) 
  
    print(llist.nthnode(7,llist))
    
