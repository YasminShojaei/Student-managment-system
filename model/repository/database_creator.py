import sqlite3

connection = sqlite3.connect("university_db.sqlite")

#
# cursor = connection.cursor()
#
# cursor.execute("SQL")
#
# connection.commit()
#
# cursor.close()
connection.close()