x = int(input("Введите колличество строк матрицы:"))
y = int(input("Введите колличество столбцов матрицы:"))
ListA = []
for i in range(x):
    ListA1 = []
    for k in range(y):
        a = int(input("Заполните матрицу значениями:"))
        ListA1.append(a)
    ListA.append(ListA1)
# Поиск максимального числа главной диагонали
maximum = ListA[0][0]
for i in ListA:
    print (i)
for i in range(0,len(ListA)):
    if maximum < ListA[i][i]:
        maximum = ListA[i][i]
print ("Максимальное число диагонали", maximum)
# поиск кол-ва отрицательных эл-тов под главной диагональю
p = 0
for i in range(0,len(ListA)):
    for j in range(0,len(ListA)):
        if j >= i:
            break
        else:
            if ListA[i][j] < 0:
                p += 1
print("Колличество отрицательных элементов под главной диагональю",p)