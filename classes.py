class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I'm {self.name}")


john = Person("John Smith")
john.talk()
Bob = Person("Bob marley")
Bob.talk()
