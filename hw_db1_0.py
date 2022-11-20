import sqlite3
db_per1 = sqlite3.connect("database.db")
db_per2 = db_per1.cursor()
db_per2.execute("""CREATE TABLE IF NOT EXISTS directory (
FULL_NAME TEXT,
ACADEMIC_DEGREE TEXT,
SCIENTIFIC_DIRECTION TEXT,
PLACE_OF_WORK TEXT,
CHAIR TEXT,
JOB_TITLE TEXT,
COUNTRY TEXT,
CITY TEXT,
ADDRESS TEXT,
WORK_PHONE TEXT,
EMAIL TEXT
)""")
db_per3 = db_per1.cursor()
db_per3.execute("""CREATE TABLE IF NOT EXISTS participants (
SPEAKER TEXT,
DATE_OF_SENDING_THE_INVITATION TEXT,
APPLICATION_DATE TEXT,
TOPIC TEXT,
abstrac_receipt_mark TEXT,
arrival_date TEXT,
need_for_a_hotel TEXT,
departure_date TEXT
)""")
db_per1.commit()