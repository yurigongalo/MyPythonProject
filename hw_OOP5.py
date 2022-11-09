class Car:
    def __init__(self, model_name = "E38 ", brand = "Бумер ", drive_unit = "front "):
        self.model_name = model_name
        self.brand = brand
        self.drive_unit = drive_unit
    def Info(self):
        print("Марка автомобиля " + self.brand + "Название модели "+ self.model_name + "Привод: " + self.drive_unit)

class BMV(Car):
    def __init__(self, model_name):
        self.model_name = model_name
    def Info(self):
        print("Название модели " + self.model_name)

class BMV1(Car):
    def __init__(self, brand):
        self.brand = brand
    def Info(self):
        print("Марка автомобиля: " + self.brand)

class BMV2(Car):
    def __init__(self, drive_unit):
        self.drive_unit = drive_unit
    def Info(self):
        print("Привод: " + self.drive_unit)

