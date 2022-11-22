import sqlite3
conn = sqlite3.connect("database.db")
curs = conn.cursor()
tb1 = """CREATE TABLE IF NOT EXISTS directory(FULL_NAME TEXT,ACADEMIC_DEGREE TEXT, SCIENTIFIC_DIRECTION TEXT, PLACE_OF_WORK TEXT, \
CHAIR TEXT, JOB_TITLE TEXT, COUNTRY TEXT, CITY TEXT, ADDRESS TEXT, WORK_PHONE TEXT, EMAIL TEXT);"""
curs.execute(tb1)
tb2 = """CREATE TABLE IF NOT EXISTS  participants(SPEAKER TEXT, DATE_OF_SENDING_THE_INVITATION TEXT, APPLICATION_DATE TEXT, \
TOPIC TEXT, abstrac_receipt_mark TEXT, arrival_date TEXT, need_for_a_hotel TEXT, departure_date TEXT);"""
curs.execute(tb2)
tb3 = """CREATE TABLE IF NOT EXISTS  information(conference_name TEXT, the_date_of_the TEXT, location TEXT, organizers TEXT, \
sponsors TEXT, amount_of_days TEXT, number_of_participants TEXT, number_of_speakers TEXT);"""
curs.execute(tb3)
conn.commit()
#Вывод всех данных из таблицы
per1 = """SELECT * FROM directory"""
curs.execute(per1)
sel1 = curs.fetchall()
print(sel1)
per2 = """SELECT * FROM participants"""
curs.execute(per2)
sel2 = curs.fetchall()
print(sel2)
per3 = """SELECT * FROM information"""
curs.execute(per3)
sel3 = curs.fetchall()
print(sel3)
#Выборочный запрос
per4 = """SELECT * FROM directory WHERE PLACE_OF_WORK='Kobrinskaya CRB';"""
curs.execute(per4)
sel4 = curs.fetchall()
print(sel4)
per5 = """SELECT * FROM information"""
curs.execute(per5)
sel5 = curs.fetchmany(2)
per6 = """SELECT * FROM participants;"""
curs.execute(per6)
sel6 = curs.fetchone()
print(sel6)
# conn.commit()
curs.close()
conn.close()