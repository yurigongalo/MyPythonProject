class Animal:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    def hello(self):
        print("Животное: " + self.name)
    def Sex(self):
        print('его пол: ' + self.sex)
    def Age(self):
        print('возраст животного: ' + self.age)
class _Tiger(Animal):# пример protected инкапсуляции
    def __init__(self, name, sex, age):
        super().__init__(name,sex, age)
    def _run(self):# пример protected инкапсуляции
        print("Тигр бегает")
class Monkey(Animal):
    def __init__(self,name,sex,age):
        super().__init__(name,sex,age)
    def habitat(self):
        print("Обитает в дикой природе")
class Wolf(Animal):
    def __init__(self,name,sex,age):
        super().__init__(name,sex,age)
    def mult(self):
        print("Является героем мультфильма")