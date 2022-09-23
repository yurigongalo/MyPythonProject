MyList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print("Прежний список\n", MyList)
a = input("Введите нижний элемент интервала ")
b = input("Введите верхний элемент интервала ")
c=0
k=0
for i in MyList:
    if int(a)<=i<=int(b):
        c=c+1
        MyList.remove(i)
while k<c:
    MyList.append(0)
    k=k+1
print("Обновленный список", MyList)
print ("Кол-во проходов: ",c)
