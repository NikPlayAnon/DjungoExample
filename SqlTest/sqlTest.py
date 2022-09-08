import mysql.connector
from mysql.connector import (connection)

conn = mysql.connector.connect(
#cnx = connection.MySQLConnection(
    host="localhost",
    database="shope",
    user="root",
    password='for(intI=0;I<k;I++){};'
)

#create_db_query = "insert into shope.clients(phoneNum,OperatorCode,timeLine) values (78978978978,897,2);"

cursor=conn.cursor()
cursor.execute("insert into shope.clients(phoneNum,OperatorCode,timeLine) values (78978978978,897,2);")
#cursor.execute("select * from shope.clients;")
#myresoult = cursor.fetchall()
conn.commit()
print("lookup")
