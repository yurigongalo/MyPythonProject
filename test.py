text = input('Введите текст:')
result = {}
# Разбивает строку на части, и проведем итерацию по каждому слову
for txt in text.split():
    # Если слово уже встречалось, прибавим +1
    if not result.get(txt) == None:
        result[txt] += 1
        # Если не встречалось, присвоим ему ровно 1
    else:
        result[txt] = 1

# Выводим результат
for key, value in result.items():
    print(f'Слово: {key}, Количество: {value}')