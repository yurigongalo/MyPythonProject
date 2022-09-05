chislo=input("Введите трехзначное число")
try:
    a = int(chislo[0])
    b = int(chislo[1])
    c = int(chislo[2])
except ValueError:
    print("Вы ввели не число")
else:
d=a+b+c
print("Сумма трех введенных чисел"+" "+str(d))