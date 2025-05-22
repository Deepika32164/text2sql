import sqlite3
connection=sqlite3.connect("students.db")
cursor=connection.cursor()
table_info="Create table STUDENTS(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);"
cursor.execute(table_info)
cursor.execute("Insert Into STUDENTS values('Krish','Data Science','A',90)")
cursor.execute("Insert Into STUDENTS values('Sudhanshu','Data Science','B',100)")
cursor.execute("Insert Into STUDENTS values('Darius','Data Science','A',86)")
cursor.execute("Insert Into STUDENTS values('Vikash','DEVOPS','A',50)")
cursor.execute("Insert Into STUDENTS values('Dipesh','DEVOPS','A',35)")
print("The inserted records are")
data=cursor.execute("select * from STUDENTS")
for row in data:
    print(row)
connection.commit()
connection.close()