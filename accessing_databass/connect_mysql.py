import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="employee")
                     
# Create a Cursor object
cur = db.cursor()

cur.execute("SELECT * FROM employee")

# Print all the first cell of all the rows
for row in cur.fetchall():
     print row[0]
     
db.close()                         