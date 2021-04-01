class House:
    def accept(self, visitor_object):
        # check the object and call object's visit method
        # provide calling object in argument Home in this case
        visitor_object.visit(self)

    def work_on_plumbing(self, plumber_object):
        print("{} worked on by {}".format(self, plumber_object))

    def work_on_electricity(self, electric_object):
        print("{} worked on by {}".format(self, electric_object))

    def __str__(self):
        return self.__class__.__name__


class Visitor:
    def __str__(self):
        return self.__class__.__name__

class Plumber(Visitor):
    def visit(self, target_caller):
        target_caller.work_on_plumbing(self)

class Electrician(Visitor):
    def visit(self, target_caller):
        target_caller.work_on_electricity(self)

house = House()
electrician = Electrician()
plumber = Plumber()

house.accept(electrician)
house.accept(plumber)
