class NameGreeter2:
    PREFIX = "Hello "
    def __init__(self, name):
        self.my_name= name

    def greeter(self):
        print(self.PREFIX, self.my_name)

p1 = NameGreeter2("Gvido")
p1.greeter()
p1.PREFIX = "Goodby "
p1.greeter()
p2 = NameGreeter2("Bizly")
p2.greeter()
p3 = NameGreeter2("Raymond")
p3.greeter()