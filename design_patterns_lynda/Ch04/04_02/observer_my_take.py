class ObserverTracker:
    def __init__(self):
        self._observers_list = []

    def attach_observer(self, observer):
        if observer not in self._observers_list:
            self._observers_list.append(observer)

    def detach_observer(self, observer):
        try:
            self._observers_list.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers_list:
            observer.update(self)


class CoreEntity(ObserverTracker):

    def __init__(self, name=""):
        ObserverTracker.__init__(self)
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, new_value):
        self._temp = new_value
        self.notify()

class ObserverEntity:
    def __init__(self, unique_num):
        self.unique_num = unique_num

    def update(self, entity):
        print("Observer ID: {} is reporting change in temp of {}. Current temp is {}".format(self.unique_num, entity._name, entity._temp))

core_entity1 = CoreEntity("first_entity")
core_entity2 = CoreEntity("second_entity")

observer_entity1 = ObserverEntity(1)
observer_entity2 = ObserverEntity(2)

core_entity1.attach_observer(observer_entity1)
core_entity1.attach_observer(observer_entity2)

core_entity2.attach_observer(observer_entity1)
core_entity2.attach_observer(observer_entity2)

core_entity1.temp = 80
core_entity2.temp = 90
print(core_entity2.temp)
