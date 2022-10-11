#Открываем заранее созданный файл и помещаем его содержимое в переменную
f = open('class.txt', 'r')
content = f.read()
f.close() #Закрываем файл
# Обращаем содержимое переменной с список и работаем и "форматируем" его
content = content.split("\n")
pupils = []
for line in content:
    line = line.split(" ")
    pupils.append([line[0], line[1], int(line[2])])
srednia = 0
print("Ниже 3 баллов:")
for p in pupils:
    srednia = srednia + int(p[2])
    if p[2] < 3:
        print(p[0],p[1],p[2]) #Ввыводим того, у кого самая низка оценка
srednia = srednia / len(pupils) #Считаем и выводим среднюю
print("Средняя оценка по классу:",srednia)