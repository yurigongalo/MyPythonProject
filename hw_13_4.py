a = int(input("Введите 1е число"))
b = int(input("Введите 2e число"))
c = 0
if a-b==1 or b-a==1:
    print("Само минимальное и максимальное число не включены в вывод по условиям задачи")

elif a < b:
    for i in range (a+1,b):
        c += i
    print(c)
elif a == b:
    print("Числа равны. Условие не выполнено")
else:
    for i in range (b+1, a):
        c += i
    print(c)
