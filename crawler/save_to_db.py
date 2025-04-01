import os
import csv
import pymysql
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = pymysql.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    db=DB_NAME,
    charset="utf8mb4"
)
cursor = conn.cursor()

# 형용사 저장
with open("../emotional_adjectives.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        word = row[0]
        cursor.execute("INSERT INTO adjectives (word) VALUES (%s)", (word,))

# 명사 저장
with open("../emotional_nouns.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        word = row[0]
        cursor.execute("INSERT INTO nouns (word) VALUES (%s)", (word,))

conn.commit()
cursor.close()
conn.close()

print(">>>>> 형용사/명사 저장 완료 <<<<<<")
