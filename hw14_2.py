myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_length=len(myList)
sumOfElements=0
for i in myList:
    sumOfElements=sumOfElements+int(i)
SrArifmet=sumOfElements/list_length
print("Колличество элементовтов списка:", list_length)
print("Сумма всех элементов списка:", sumOfElements)
print("Средне Арифметическое значение:", SrArifmet)
print("Перечень элементов списка, которые меньше среднего арифместического:")
for k in myList:
    if k<SrArifmet:
        print(k, end=" ")