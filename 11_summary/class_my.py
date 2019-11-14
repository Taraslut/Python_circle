class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __str__(self):
        return f"Dog {self.name} can trick " + " ".join(self.tricks)


marv = Dog("Marv")
marv.add_trick("jump")
print(marv)

sem = Dog("Sem")
sem.add_trick("swipe")
print(sem)
print(marv)