class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def hello(self):
        print("привет " + self.name + " ваш возраст " + str(self.age))

human1 = Person(32,"Юра")
human1.hello()
