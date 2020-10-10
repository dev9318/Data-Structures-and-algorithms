class binaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percolateup(self,i):
        while(i//2>0):
            if (self.heapList[i] < self.heapList[i//2]):
                temp = self.heapList[i]
                self.heapList[i] = heapList[i//2]
                self.heapList[i//2] = temp
            else:
                return
            i = i//2
        return
    def insert(self, value):
        self.heapList.append(value)
        self.currentSize += 1
        self.percolateup(self.currentSize)

    def  