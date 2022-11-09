class Car:
    def __init__(self, model_name, brand):
        self.model_name = model_name
        self.brand = brand

    def Info(self):
        print("Марка автомобиля " + self.brand + "Название модели "+ self.model_name)

class BMV(Car):
    def __init__(self, model_name):
        self.model_name = model_name
    def Info(self):
        print("Название модели " + self.model_name)

bmv1 = BMV("A6")
bmv1.Info()

car1 = Car("M8", "Audi ")
car1.Info()

