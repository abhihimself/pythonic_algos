import random
from queue_implementation import Queue
import time

class Printer():
    def __init__(self,page_per_minute):
        self.ppm=page_per_minute
        self.current_task=None
        self.timeremaining=0

    def tick(self):
        if self.current_task != None:
            self.timeremaining=self.timeremaining-1
        if self.timeremaining<=0:
            self.current_task=None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def startnext(self,newtask):
        self.current_task=newtask
        self.timeremaining=newtask.get_pages()*60/self.ppm


class Task():
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)

    def getstamp(self):
        return  self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self,currenttime):
        return currenttime-self.timestamp

def simulator(timeduration,ppm):
    task_queue=Queue()
    print_object=Printer(ppm)
    waiting_list=[]

    for eachsecond in range(timeduration):
        if istask() is True:
            newtask=Task(eachsecond)
            task_queue.enqueue(newtask)
        if not print_object.busy() and not task_queue.isEmpty():
            current_task=task_queue.dequeue()
            waiting_list.append(current_task.wait_time(eachsecond))
            print_object.startnext(current_task)

        print_object.tick()

    average_wait=sum(waiting_list)/len(waiting_list)
    print("Average wait time {}. Number of pending task {}".format(average_wait,len(waiting_list)))

def istask():
    num=random.randrange(1,181)
   # print(num)
    if num==180:
        return True
    else:
        return False

for i in range(10):
    simulator(3600,5)
