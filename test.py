x = int(input("Введите колличество строк матрицы:"))
y = int(input("Введите колличество столбцов матрицы:"))
ListA = []
for i in range(x):
    ListA1 = []
    for k in range(y):
        a = int(input("Заполните матрицу значениями:"))
        ListA1.append(a)
    ListA.append(ListA1)
    for k in ListA:
        if k==i:
            print(n)