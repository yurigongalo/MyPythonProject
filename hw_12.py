print("Это программа сравнения возрастов 2х человек\nВведите полную дату рождения 1-го человека:")
bd1=input("День ")
bm1=input("Месяц ")
by1=input("Год ")
print("Введите полную дату рождения 2-го человека:")
bd2=input("День ")
bm2=input("Месяц ")
by2=input("Год ")
if int(by1)<int(by2) or int(by1)==int(by2) and int(bm1)<int(bm2) or int(by1)==int(by2) and int(bm1)==int(bm2) and int(bd1)<int(bd2):
    print("Первый человек старше второго человека")
elif int(by1)==int(by2) and int(bm1)==int(bm2) and int(bd1)==int(bd2):
    print("1-й и 2-й человек родились в один день")
else:
    print("Второй человек старше первого человека")