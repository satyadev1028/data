'''
	Used 4 spaces instead of tab for supressing pylint errors
	This Script will all records to the Symbols table
	Don't re-run this script. If you want to then drop this table and create the table again.
	drop table symbols;
	create table symbols(id int primary key auto_increment,name varchar(100),symbol varchar(20));
'''

import mysql.connector

FILE = open("NASDAQ.txt", "r+")

MYDB = mysql.connector.connect(host="localhost", user="root", passwd="arena", database="dip")

LINES = FILE.readlines()
for line in LINES:
    words = line.split(',')
    mycursor = MYDB.cursor()
    sql = "INSERT INTO symbols (name, symbol) VALUES (%s, %s)"
    val = (words[1], words[0])
    mycursor.execute(sql, val)
    MYDB.commit()
