import sqlite3
conn = sqlite3.connect("database.db")
curs = conn.cursor()
# Обновление данных
upd1 = """UPDATE directory SET FULL_NAME= 'Пётр Петров' WHERE FULL_NAME= 'Petr Petrov';"""
upd2 = """UPDATE directory SET FULL_NAME= 'Сидор Сидоров' WHERE FULL_NAME= 'Sidiriv Sidor';"""
upd3 = """UPDATE directory SET FULL_NAME= 'Сергей Сергеев' WHERE FULL_NAME= 'Sergey Sergeev';"""
curs.execute(upd1)
curs.execute(upd2)
curs.execute(upd3)
upd4 = """UPDATE information SET conference_name= 'Лучшая конференция' WHERE conference_name= 'The best conference';"""
upd5 = """UPDATE information SET conference_name= 'Лучшая и лучших' WHERE conference_name= 'the best of the best';"""
upd6 = """UPDATE information SET conference_name= 'Супер-пупер конференция' WHERE conference_name= 'Puper puper conference';"""
curs.execute(upd4)
curs.execute(upd5)
curs.execute(upd6)
upd7 = """UPDATE participants SET SPEAKER= 'Иванов Иван' WHERE SPEAKER= 'Ivanov Ivan';"""
upd8 = """UPDATE participants SET SPEAKER= 'Пол Дайк' WHERE SPEAKER= 'Paul Dike';"""
upd9 = """UPDATE participants SET SPEAKER= 'Александр Александров' WHERE SPEAKER= 'Alyaxander Alyaxandrov';"""
curs.execute(upd7)
curs.execute(upd8)
curs.execute(upd9)
# Удаление данных
del1 = """DELETE FROM directory WHERE FULL_NAME= 'Ivan Sidorov' """
del2 = """DELETE FROM directory WHERE FULL_NAME= 'Sergey Sergeev' """
del3 = """DELETE FROM directory WHERE FULL_NAME= 'Pavel Pavlov' """
del4 = """DELETE FROM information WHERE conference_name= 'Medical life' """
del5 = """DELETE FROM information WHERE conference_name= 'The best of the best of the best' """
del6 = """DELETE FROM information WHERE conference_name= 'conference of the best' """
del7 = """DELETE FROM participants WHERE SPEAKER= 'Ivanov Ivan' """
del8 = """DELETE FROM participants WHERE SPEAKER= 'Sidiriv Sidor' """
del9 = """DELETE FROM participants WHERE SPEAKER= 'Petr Petrov' """
curs.execute(del1)
curs.execute(del2)
curs.execute(del3)
curs.execute(del4)
curs.execute(del5)
curs.execute(del6)
curs.execute(del7)
curs.execute(del8)
curs.execute(del9)

conn.commit()
curs.close()
conn.close()