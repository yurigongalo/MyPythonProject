
myList = [-11, -10, -8, -1, 2, 6, 7, 8, 9]
# print("Был задан следующий список:")
# print(myList)
list_length=len(myList)
sumOfElements=0
for i in range(list_length):
    if i>0 and i%2==0:
        sumOfElements=sumOfElements+myList[i]
print("Сумма четных положительных элементов списка:", sumOfElements)