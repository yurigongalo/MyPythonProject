x = int(input("Введите колличество строк матрицы:"))
y = int(input("Введите колличество столбцов матрицы:"))
ListA = []
for i in range(x):
    ListA1 = []
    for k in range(y):
        a = int(input("Заполните матрицу значениями:"))
        ListA1.append(a)
    ListA.append(ListA1)
p = 0
for i in range(0,len(ListA)):
    for j in range(0,len(ListA)):
        if j >= i:
            break
        else:
            if ListA[i][j] < 0:
                p += 1
print(p)
