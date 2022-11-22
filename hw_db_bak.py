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
ins11 = """INSERT INTO directory(FULL_NAME, ACADEMIC_DEGREE, SCIENTIFIC_DIRECTION, PLACE_OF_WORK, CHAIR, JOB_TITLE, COUNTRY, CITY, \
ADDRESS, WORK_PHONE, EMAIL) VALUES("Petr Petrov", "Doctor", "psychiatry", "Kobrinskaya CRB", "psychiatry", "Zav Otdeleniem", "Belarus", \
"Kobrin", "Kobrin, Parkovaya sr, d1", "2-31-31", "petrov@kobincrb.by");"""

ins12 = """INSERT INTO directory(FULL_NAME, ACADEMIC_DEGREE, SCIENTIFIC_DIRECTION, PLACE_OF_WORK, CHAIR, JOB_TITLE, COUNTRY, CITY, \
ADDRESS, WORK_PHONE, EMAIL) VALUES("Ivan Ivanov", "Doctor", "Terapevt", "Kobrinskaya CRB", "Medicina", "Zam Zav Otdeleniem", "Belarus", \
"Kobrin", "Kobrin, Parkovaya str, d2", "2-32-32", "ivanov@kobincrb.by");"""

ins13 = """INSERT INTO directory(FULL_NAME, ACADEMIC_DEGREE, SCIENTIFIC_DIRECTION, PLACE_OF_WORK, CHAIR, JOB_TITLE, COUNTRY, CITY, \
ADDRESS, WORK_PHONE, EMAIL) VALUES("Sidor Sidorov", "Doctor", "Vrach", "Brestskaya CRB", "Medicina", "Zav Otdeleniem", "Belarus", \
"Brest", "Brest, Parkovaya str, d2", "22-32-32", "sidirov@brestcrb.by");"""

ins14 = """INSERT INTO directory(FULL_NAME, ACADEMIC_DEGREE, SCIENTIFIC_DIRECTION, PLACE_OF_WORK, CHAIR, JOB_TITLE, COUNTRY, CITY, \
ADDRESS, WORK_PHONE, EMAIL) VALUES("Ivan Sidorov", "Doctor", "Vrach", "Brestskaya CRB", "Medicina", "Zam Zav Otdeleniem", "Belarus", \
"Brest", "Brest, Parkovaya str, d8", "24-32-32", "sidiroivan@brestcrb.by");"""

ins15 = """INSERT INTO directory(FULL_NAME, ACADEMIC_DEGREE, SCIENTIFIC_DIRECTION, PLACE_OF_WORK, CHAIR, JOB_TITLE, COUNTRY, CITY, \
ADDRESS, WORK_PHONE, EMAIL) VALUES("Sergey Sergeev", "Doctor", "Vrach", "Pinskaya CRB", "Medicina", "Zav Otdeleniem", "Belarus", \
"Pinsk", "Pinsk, PPinskaya str, d9", "34-32-32", "sergeev@pinskcrb.by");"""

ins16 = """INSERT INTO directory(FULL_NAME, ACADEMIC_DEGREE, SCIENTIFIC_DIRECTION, PLACE_OF_WORK, CHAIR, JOB_TITLE, COUNTRY, CITY, \
ADDRESS, WORK_PHONE, EMAIL) VALUES("Pavel Pavlov", "Doctor", "Vrach", "Pinskaya CRB", "Medicina", "Zam Zav Otdeleniem", "Belarus", \
"Pinsk", "Pinsk, Sovetskaya str, d3", "44-32-34", "pavlov@pinskcrb.by");"""
curs.execute(ins11)
curs.execute(ins12)
curs.execute(ins13)
curs.execute(ins14)
curs.execute(ins15)
curs.execute(ins16)
conn.commit()
curs.close()
conn.close()