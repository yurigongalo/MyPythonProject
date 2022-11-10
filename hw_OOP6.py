from abc import abstractstaticmethod
class Animal():
    def __init__(self):
        pass
    def WakesAP(self):
        pass
    def Awake(self):
        pass
    def FallsAsleep(self):
        pass
class Dog(Animal):
    def __init__(self):
        pass
    def WakesAP(self):
        print("Собака просыпается")
    def Awake(self):
        print("Собака бодрствует")
    def FallsAsleep(self):
        print("Собака засыпает")

DogLife1 = Dog()
DogLife1.WakesAP()
DogLife1.Awake()
DogLife1.FallsAsleep()