class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.percUp(self.currentSize)

    def percUp(self, current_size):
        i = current_size
        while i//2 > 0:
            if self.heapList[i//2] < self.heapList[i]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2

    def delMin(self):
        min_item = self.heapList[1]
        max_item = self.heapList[self.currentSize]
        self.heapList[1] = max_item
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return min_item

    def percDown(self, i):
        while i <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def minChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2+1]<self.heapList[i*2]:
                return i*2+1
            else:
                return i*2

    def buildHeap(self, alist):




bh = BinHeap()


print(bh.delMin())

print(bh.delMin())

print(bh.delMin())

print(bh.delMin())

