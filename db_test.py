import mysql.connector as dbapi


conn = dbapi.Connect(host='127.0.0.1', port='3306',
                     user='root', database='test')
cur = conn.cursor()

'''cur.execute("SELECT * FROM first")
id = 2
name = 'testname'
gen = 'M'
cur.execute('insert into first values ("%s", "%s", "%s");' % (id, name, gen))'''


cur.execute(
    "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='test' AND TABLE_NAME='test';")

myresult = cur.fetchall()
print(myresult)
