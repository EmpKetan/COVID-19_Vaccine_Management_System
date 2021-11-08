import mysql.connector
passwrd=input("Enter your systems mysql password :- ")
mydb = mysql.connector.connect(user="root", password=passwrd,host="localhost")
cur=mydb.cursor()

cur.execute("create database if not exists vaccinerecord;")
cur.execute("use vaccinerecord;")

cur.execute("create table if not exists proflogi(profuser_name varchar(50),profpw varchar(30));")
cur.execute("insert into proflogi values('admin','admin123');")

cur.execute("create table if not exists patlogi(patuser_name varchar(50),patpw varchar(30));")
cur.execute("insert into patlogi values('admin','admin123');")

cur.execute("create table if not exists profdata(prof_id int(20) primary key,prof_name varchar(50),prof_dep varchar(30));")

cur.execute("create table if not exists patdata(pat_id int(20) primary key,pat_name varchar(50),pat_age int(10),pat_status varchar(20),pat_vacproid int(30),pat_vacpro varchar(30),pat_profcareid int(20),pat_fshot date,pat_sshot date);")

cur.execute("create table if not exists vacpro(vacproid int(30) unique,vacpro varchar(30),vacprocost int(10));")

print("SQL quries completed sucessfully")
