f = open('class.txt', 'r')
content = f.read()
f.close()
content = content.split("\n")
pupils = []
print (content)
for line in content:
    line = line.split(" ")
    pupils.append([line[0], line[1], int(line[2])])
srednia = 0
print("Ниже 3 баллов:")
for p in pupils:
    srednia = srednia + int(p[2])
    if p[2] < 3:
        # print(f"{p[0]} {p[1]}: {p[2]}")
        print(p[0],p[1],p[2])
srednia = srednia / len(pupils)
print("Средняя оценка по классу:",srednia)