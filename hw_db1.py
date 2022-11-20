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
curs.close()
conn.close()