import math
def treug(a, b, c):
    pl = (a+b+c)/2
    return math.sqrt(pl * (pl-a) * (pl-b) * (pl-c))
def krug(r):
    return math.pi * r**2
def pryamoug(a, b):
    return a*b
vybor = input("Круг(1), прямоугольник(2) или треугольник(3): ")
if vybor == '1':
    rad = float(input("Радиус: "))
    print("Площадь круга: ", krug(rad))
elif vybor == '2':
    l = float(input("Длина: "))
    w = float(input("Ширина: "))
    print("Площадь прямоугольника: ", pryamoug(l,w))
elif vybor == '3':
    stor1 = float(input("Первая сторона: "))
    stor2 = float(input("Вторая сторона: "))
    stor3 = float(input("Третья сторона: "))
    print("Площадь треугольника: ", treug(stor1,stor2,stor3))
else:
    print("Ошибка ввода")