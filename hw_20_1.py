text = input('Введите текст:')
result = {}
# Разобьем строку по отдельным словам
for txt in text.split():
    # Если значенме в словаре втречалось, прибавим +1
    if not result.get(txt) == None:
        result[txt] += 1
        # Если не встречалось, присвоим ему ровно 1
    else:
        result[txt] = 1
# Получаем результат
for key, value in result.items():
    print('Слово:',key,'Количество:',value)