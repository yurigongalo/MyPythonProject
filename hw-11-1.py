a=int(input("Введите минимальное число"))
b=int(input("Введите максимальное число"))
c=int(input("Введите шаг"))
for i in range(a,b+1,c):
    print((i), end=" ")
