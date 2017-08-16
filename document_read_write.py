# -*- coding:utf-8 -*-

def document_write(filename):
    try:
        file_cur = open(filename,'w',encoding='utf-8')
        # write
        file_cur.write(str(something))
        file_cur.close()
    except:
        print("write exception")

def document_read(filename):
    try:
        file_cur = open(filename,'r',encoding='utf-8')
        #read
        chunk = eval(file_cur.read())
    except:
        print("read exception")
