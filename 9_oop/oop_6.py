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


p1 = ExtraPerson("Jon", 3)
p1.info()
p1.change_age(150)
p1.info()