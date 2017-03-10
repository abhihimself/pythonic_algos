from queue_implementation import Queue

def hotPotato(namelist,num):
    q=Queue()
    for item in namelist:
        q.enqueue(item)

    while q.size() > 1:
        for i in range(num):
            candidate=q.dequeue()
            q.enqueue(candidate)

        q.dequeue()

    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

