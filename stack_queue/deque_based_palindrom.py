from deque_implementation import Deque

def palchecker(text):
    d=Deque()
    for i in text:
        d.addFront(i)

    matched=True
    while d.size()>1 and matched:
        front=d.removeFront()
        rear=d.removeRear()
        if front!=rear:
            matched=False

    print(d.size())
    if d.size()==1 and matched==True:
        return True
    else:
        return False

print(palchecker('lsdkjfskf'))
