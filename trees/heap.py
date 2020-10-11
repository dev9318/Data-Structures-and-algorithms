class binaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percolateup(self,i):
        while(i//2>0):
            if (self.heapList[i] < self.heapList[i//2]):
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            else:
                return
            i = i//2
        return
    def insert(self, value):
        self.heapList.append(value)
        self.currentSize += 1
        self.percolateup(self.currentSize)

    def percolatedown(self,i):
        while(i*2 <= self.currentSize):
            m = self.minChild(i)
            if (self.heapList[i] > self.heapList[m]):
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[m]
                self.heapList[m] = temp
            i = m

    def minChild(self,i):
        if (i*2+1 >self.currentSize):
            return i*2
        elif (self.heapList[2*i]<self.heapList[2*i+1]):
            return 2*i
        else:
            return 2*i + 1

    def delMin(self):
        retmin = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percolatedown(1)
        return retmin
    
    def buildHeap(self,hlist):
        self.currentSize = len(hlist)
        self.heapList = [0] + hlist[:]
        i = len(hlist) // 2
        while(i>0):
            self.percolatedown(i)
            i -= 1

    def printHeap(self):
        print(self.heapList)
    
if __name__ == "__main__":
    heap = binaryHeap()
    heap.buildHeap([6,3,2,4,7,1])
    heap.printHeap()
    print(heap.delMin())
    heap.printHeap()