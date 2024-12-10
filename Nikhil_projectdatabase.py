import pymysql


conn=pymysql.connect(host='localhost',user='root',password='Nikhil@141937')
cur=conn.cursor()
cur.execute("create database mynewproject")
print("table is created")
conn.close()
