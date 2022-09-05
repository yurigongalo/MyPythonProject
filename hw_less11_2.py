birth_day=input("Введите день рождения ")
birth_month=input("Введите месяц рождения ")
birth_year=input("Введите год рождения ")
cur_day=5 # Текущий день
cur_month=9 # Текущий месяц
cur_year=2022 # Текущий год
if cur_month==int(birth_month) and cur_day>=int(birth_day) or cur_month>int(birth_month):
    my_year=cur_year-int(birth_year)
else:
    my_year = cur_year-int(birth_year)-1
print("Ваш возраст"+" "+str(my_year)+" "+"полных лет")
