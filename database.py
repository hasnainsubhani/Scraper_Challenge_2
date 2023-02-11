import mysql.connector as conn
import csv

mydb = conn.connect(host="localhost",username="root",password="hasnain@@1",database="testdb")
cursor = mydb.cursor()
cursor.execute("create table if not exists video_details(video_Id int AUTO_INCREMENT PRIMARY KEY, video_Title varchar(50),video_description varchar(500),likes int,video_url varchar(100))")

#cursor.execute("show tables")
#_tables = cursor.fetchall()
#print(_tables)

val = ""
query = ""
with open('video_details.csv','r') as f:
    _data = csv.reader(f,delimiter='\n')
    for row in _data:
        val = '\'' +str(row[0]).replace(',','\',\'')+'\''
        query = "insert into cars(video_Title,video_description,likes,video_url) values("+ val + ")"
        cursor.execute(query)
    mydb.commit()
f.close() 


