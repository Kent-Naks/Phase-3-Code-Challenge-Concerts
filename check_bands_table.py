import sqlite3

# Replace 'path_to_your_database' with the actual path where your concerts.db file is located
connection = sqlite3.connect('concerts.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(tables)
connection.close()
