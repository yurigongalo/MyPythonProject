chislo=int(input("Введите число"))
obr=0
while chislo>0:
    cifra=chislo%10
    chislo=chislo//10
    obr=obr*10
    obr=obr+cifra
print("Обратное число: "+str(obr))