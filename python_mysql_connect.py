# -*- coding:utf-8 -*-

import MySQLdb

#connect to remote mysql
def mysql_connect(host,user,passwd,db,port,sql):
    try:
        conn=MySQLdb.connect(host,user,passwd,db,port,sql)
        cur=conn.cursor()
        cur.execute("select * from driver limit 10")
        row=cur.fetchall()
        print row
    except MySQLdb.Error,e:
        print "Mysql error:%s"%str(e)
