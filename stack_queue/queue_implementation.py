class Queue():
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items==[]

if __name__=='__main__':
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    q.dequeue()

    while not q.isEmpty():
        a=q.dequeue()
        print(a)

