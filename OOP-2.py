class Animal:
    def __init__(self, name, sex, age, tip, habitat):
        self.name = name
        self.sex = sex
        self.age = age
        self.tip = tip
        self.habitat = habitat
    def hello(self):
        print("Животное: " + self.name)
    def Sex(self):
        print('его пол: ' + self.sex)
    def Age(self):
        print('возраст животного: ' + self.age)
    def Tip(self):
        print('Хищник или травоядное?: ' + self.tip)
    def Habibat(self):
        print("Среда обитания: " + self.habitat)
Animal1 = Animal("Лев","Мужчина","Взрослый уже","Хищник","Дикая природа")
Animal1.hello()
Animal1.Sex()
Animal1.Age()
Animal1.Tip()
Animal1.Habibat()


