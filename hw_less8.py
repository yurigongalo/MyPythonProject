# Домашнее задание. Ответы на 1 вопрос
str1 = 'Hello' # Способ обозначения строк с одинарными кавычками
str2 = "World" # Аналогичный способ с двойными кавычками
# Домашнее задание. Ответы на 2 вопрос
print(str1, str2) # Демонстарция вывода сложения 2х с трок
print(str1 + " " + str2) # Демонстарция вывода сложения 2х с трок
name = 'Юрий'
age = 32
# Далее так же будет демонстрация вывода сложения строк
info = 'Меня зовут' + " " + name + ', мне' + " " + str(age) + " " + "года"
print(info)
# Демонстрация повторения строки
print((str(age) * 3))
print("Проверка\tтабуляции") #При помощи последовательности \t
print ("Меня зовут" + " " + name + "," + "\nмне"+ " " + str(age)) # демонстрация перевода строки при помощи последовательности \n
print ("А сейчас попробую вывести свое имя в кавычках:  \"Юрий\"")
# Проверка типов данных, которые можно перевести в строку
a = 1
b = 1.11
c = True
d = None
aa = str(a)
bb = str(b)
cc = str(c)
dd = str(d)
print(type(aa))
print(type(bb))
print(type(cc))
print(type(dd))
# Все типы переменных, преобразуются в строку