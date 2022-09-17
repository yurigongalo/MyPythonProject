MyList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# print(MyList)
a = input("Введите нижний элемент интервала")
b = input("Введите верхний элемент интервала")
c=0
for i in MyList:
    if int(a)<=i<=int(b):
        c=c+1
        MyList.remove(i)
        print(i)
        print(MyList)
        print("******")
print ("Кол-во проходов: ",c)
