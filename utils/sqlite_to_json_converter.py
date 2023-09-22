import json
import sqlite3


connection = sqlite3.connect("../../data/quotes.db")
cursor = connection.cursor()
cursor.execute("select id, text from quotes;")
result = cursor.fetchall()

data = {}

for item in result:
    item_id = item[0]
    text = item[1]
    text = text.strip()
    text = text.replace(" ", " ")
    text = text.replace(" ", " ")
    print("-------------")
    print(text)
    data[item_id] = text

with open("../../data/quotes.json", "w", encoding="utf8") as outfile:
    json.dump(data, outfile, ensure_ascii=False)
