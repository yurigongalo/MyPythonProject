s = input("Введите строку:")
slovo = []
for i in s:
    slovo.append(i)
print('Введенная строка:',(slovo))
slovo1 = tuple((set(slovo)))
print("Итоговоый кортедж:",(slovo1))