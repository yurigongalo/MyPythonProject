# import datetime
# a = datetime.date(year=2000, month=1, day=1)
# b = datetime.date(year=2021, month=2, day=17)
# print(int((b-a).days / (365.2425)))

a=input("Введите день рождения")
b=input("Введите месяц рождения")
c=input("Введите год рождения")
# d=("Вы родились "+a+" числа "+b+"-го месяца "+c+" года")
# print (d)
if 1<=int(a)<=31:
    print("Данные приняты")
elif 1<=int(b)<=12:
elif 1<=int(c)<=2022:
else:
    print("Число не корректно")
