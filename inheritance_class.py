# inheritance is reusing a code
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark mf...')


class Cat(Mammal):
    def be_annoying(self):
        print('annoying asf....')


thedog = Dog()
thedog.walk()
thecat = Cat()
thecat.be_annoying()
