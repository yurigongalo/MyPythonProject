f = open('23_1.txt')
Str = 0
for i in f:
    Str += 1
    Simv = 0
    Sl = 0
    for j in i:
        if j != ' ' and Simv == 0:
            Sl += 1
            Simv = 1
        elif j == ' ':
            Simv = 0
    print("Строка:",i,len(i),'символов,',Sl,'слов,')
print('Всего строк:',Str)
f.close()