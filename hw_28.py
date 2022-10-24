sp = []
def SummaChisel(n):
    if (n == 0):
        return sp
    ch = n % 10
    sp.append(ch)
    SummaChisel(n // 10)
m = int(input("Введите число: "))
SummaChisel(m)
print("Результат:",sum(sp))