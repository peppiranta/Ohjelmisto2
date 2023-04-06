class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hello!")

John = Person('John')
print(John.name)
John.talk()