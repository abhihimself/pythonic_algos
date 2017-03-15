class Node():
    def __init__(self,data):
        self.data=data
        self.address=None

    def set_data(self,val):
        self.data=val

    def get_data(self):
        return self.data

    def set_next(self,val):
        self.address=val

    def get_next(self):
        return self.address

class UlinkedList():
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self,value):
        tmp = Node(value)
        previous=None
        current=self.head
        stop=False

        while current !=None and not stop:
            if current.get_data()>value:
                stop=True
            else:
                previous=current
                current=current.get_next()

        if previous ==None:
            tmp.set_next(self.head)
            self.head=tmp


        else:
            tmp.set_next(current)
            previous.set_next(tmp)







    def size(self):
        current=self.head
        count=0
        while(current != None):
            count+=1
            print(current.get_data())
            current=current.get_next()

        return count

    def search(self,target):
        found=False
        stop=False
        current=self.head
        while current !=None and not found and not stop:
            if current.get_data()==target:
                found=True
            elif current.get_data()>target:
                stop=True
            else:
                current=current.get_next()

        return found

    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while current !=None and not found:
            if current.get_data()==item:
                found=True
            else:
                previous=current
                current=current.get_next()
        if previous ==None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())







l=UlinkedList()
l.add(22)
l.add(52)

l.add(66)

l.add(55)
#l.remove(22)
print(l.size())

l.remove(55)
l.add(0)
print(l.size())