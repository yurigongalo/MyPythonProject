class Person:
    #Конструктор
    def __init__(self, age, name):
        self.age = age
        self.name = name
    #Метод
    def hello(self):
        print("привет " + self.name + " ваш возраст " + str(self.age))

human1 = Person(32,"Юра") # Объект на основе класса
human1.hello() # Метот этого класса
