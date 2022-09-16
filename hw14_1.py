myList = [-11, -10, -8, -1, 2, 6, 7, 8, 9]
# list_length=len(myList)
sumOfElements=0
for i in myList:
    if i>0 and i%2==0:
        sumOfElements=sumOfElements+int(i)
print("Сумма четных положительных элементов списка:", sumOfElements)