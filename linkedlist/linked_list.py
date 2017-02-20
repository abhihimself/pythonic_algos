class Node():
    def __init__(self,initdata):
        self.data=initdata
        self.next=None


    def set_data(self,newdata):
        self.data=newdata

    def set_next(self,newnext):
        self.next=newnext

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


class Linked_list():
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None

    def add(self,item):
        tmp=Node(item)
        tmp.set_next(self.head)
        self.head=tmp

    def size(self):
        current=self.head
        count=0
        while(current!=None):
            count+=1
            print(current.get_data())
            current=current.get_next()
        return count

    def search(self,target):
        current=self.head
        found=False
        while(current!=None) and not found:
            if target==current.get_data():
                found=True
            else:
                current=current.get_next()

        return found

    def remove(self,target):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.get_data()==target:
                found=True
            else:
                previous=current
                current=current.get_next()

        if previous==None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())






a=Linked_list()
a.add(15)
a.add(16)
a.add(19)
a.add(21)
print(a.size())
print(a.search(100))
a.remove(15)
a.add(42)
print(a.size())