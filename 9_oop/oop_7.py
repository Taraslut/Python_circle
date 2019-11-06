class ExtraPerson:
    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def info(self):
        print(self._name, self._age)

    def change_age(self, age):
        while True:
            if 5<age<95:
                self._age = age
                break
            else:
                print("Age must be in the 5-95 region")
                age = int(input('Enter age>>'))


class Personnn(ExtraPerson):
    email = "thms@google.com"


p1 = ExtraPerson("Jon", 3)
p1.info()
p1.change_age(15)
p1.info()
# p1.email
print(p1)

p2 = Personnn("Tom", 25 )
p2.info()
print(p2)