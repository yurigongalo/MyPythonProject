x = int(input("Введите колличество строк матрицы:"))
y = int(input("Введите колличество столбцов матрицы:"))
ListA = []
for i in range(x):
    ListA1 = []
    for k in range(y):
        a = int(input("Заполните матрицу значениями:"))
        ListA1.append(a)
    ListA.append(ListA1)
maximum = ListA[0][0]
for i in ListA:
    print (i)
for i in range(0,len(ListA)):
    if maximum < ListA[i][i]:
        maximum = ListA[i][i]
print ("Максимальное число диагонали", maximum)