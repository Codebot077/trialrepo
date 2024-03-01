import sqlite3,random

conn = sqlite3.connect("statistics.sqlite")
cursor  = conn.cursor()

# cursor.execute("Create table stats(timestamp time,speed int,distance int,temperature double,battery int)")
 cursor.execute("insert into stats values('17:30:01',45,473,31.87,72)")
 cursor.execute("insert into stats values('17:30:01',41,470,41.87,72)")
 cursor.execute("insert into stats values('17:30:01',49,471,32.87,72)")
 cursor.execute("insert into stats values('17:30:01',39,465,31.87,72)")
cursor.execute("select speed from stats")
data  = cursor.fetchall()
for i in data:
    print(i)
conn.commit()
# print(i[0])