class Person:
    def __init__(self, name, age):
        self.my_name = name
        self.age = age

    def greeting(self):
        print("Hello " + self.my_name)


example = Person("Vas'ja", 20)
example.greeting()
# print(1, example.my_name)
# example.my_name = "Taras"
# print(2, example.my_name)
# example.greeting()
p1 = Person("Taras", 16 )
p1.greeting()
example.greeting()
print(example.age)