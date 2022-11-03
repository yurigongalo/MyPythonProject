class Person:
    #Конструктор
    def __init__(self, age, name):
        self.age = age
        self.name = name
    #Метод
    def hello(self):
        print("привет " + self.name + " ваш возраст " + str(self.age))

human1 = Person(32,"Юра") # Объект на основе класса
human2 = Person(29,"Анна")
human3 = Person(4,'Ксения')
human4 = Person('10 месяцев','Ваня')
human5 = Person(2,"Мурзик")
human1.hello() # Метот этого класса
human2.hello()
human3.hello()
human4.hello()
human5.hello()
