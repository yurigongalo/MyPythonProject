import sqlite3
conn = sqlite3.connect("database.db")
curs = conn.cursor()
zap1 = """CREATE TABLE DIRECTORY(FULL_NAME TEXT,ACADEMIC_DEGREE TEXT, SCIENTIFIC_DIRECTION TEXT, PLACE_OF_WORK TEXT, CHAIR TEXT, JOB_TITLE TEXT, COUNTRY TEXT, CITY TEXT, ADDRESS TEXT, WORK_PHONE TEXT, EMAIL TEXT);"""
curs.execute(zap1)
conn.commit()
curs.close()
conn.close()