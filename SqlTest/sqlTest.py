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

def addToM(phoneNum,timeline):
    cursor=conn.cursor()
    cursor.execute(f"insert into shope.clients(phoneNum,OperatorCode,timeLine) values ({phoneNum},897,{timeline});")
    #cursor.execute("select * from shope.clients;")
    #myresoult = cursor.fetchall()
    conn.commit()
