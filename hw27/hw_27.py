import krug
import treug
import pryamoug
vybor = input("Площадь какой фигуры высчитать? Круг(1), прямоугольник(2) или треугольник(3): ")
if vybor == '1':
    rad = float(input("Введите Радиус: "))
    print("Площадь круга: ", krug.DefRad(rad))
elif vybor == '2':
    l = float(input("Введите длину: "))
    w = float(input("Введите ширину: "))
    print("Площадь прямоугольника: ", pryamoug.PlPtyamoug(l,w))
elif vybor == '3':
    stor1 = float(input("Первая сторона: "))
    stor2 = float(input("Вторая сторона: "))
    stor3 = float(input("Третья сторона: "))
    print("Площадь треугольника: ", treug.PlTreug(stor1,stor2,stor3))
else:
    print("Ошибка ввода")