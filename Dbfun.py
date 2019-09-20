import mysql.connector as mariadb
from mysql.connector import Error
import config as cfg
import datetime
import qrcode

query="INSERT INTO event_registration (fname,lname,city,num,pic,email) VALUES (%s,%s,%s,%s,%s,%s)"
query2="SELECT COUNT(*) FROM event_registration where email=%(value)s"
query3="SELECT COUNT(*) from event_registration WHERE fname =%(fname)s and num = %(num)s"
query4="INSERT INTO events_list (Title,Description,Catagory,Tags) VALUES (%s,%s,%s,%s)"
query5="SELECT * FROM events_list"



def register(fname,lname,city,num,image,email):
    try:
        print ("Connectin to mysql...")
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print ("Connection established")
        else:
            print ("Connection fail")
        cursor=conn.cursor()
        print(fname,lname,city,num,image,email)
        args=(fname,lname,city,num,image,email)
        cursor.execute(query,args)
        print("gh")
        conn.commit()
        
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print ("Connection closed")
    return "done"


def get_event():
    try:
        print ("Connectin to mysql...")
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print ("Connection established")
        else:
            print ("Connection fail")
        cursor=conn.cursor()
        cursor.execute(query5)
        rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        conn.commit()
        
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print ("Connection closed")
    return rows








def register_event(title,desc,catagory,tag):
    try:
        print ("Connectin to mysql...")
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print ("Connection established")
        else:
            print ("Connection fail")
        cursor=conn.cursor()
        
        args=(title,desc,catagory,tag)
        cursor.execute(query4,args)
        conn.commit()
        
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print ("Connection closed")
    return "done"

def check_exist(value):
    que=query2
    count=0

    try:
        print ("Connectin to mysql...")
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print ("Connection established")
        else:
            print ("Connection fail")
        cursor=conn.cursor()
        params1 = {'value':value}
        cursor.execute(que,params1)
        rows=cursor.fetchall()
        for row in rows:
            count=row[0]
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print ("Connection closed")
    if(count>=1):
        print (count)
        return True
    else:
        print (count)
        return False


def generate_qr(data):
    print(data)
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("sample_qr.jpg")

def check_entry(fname,number):
    que=query3
    count=0

    try:
        print ("Connectin to mysql...")
        conn=mariadb.connect(host=cfg.mysql['host'],user=cfg.mysql['user'],password=cfg.mysql['password'],database=cfg.mysql['db'])
        if conn.is_connected():
            print ("Connection established")
        else:
            print ("Connection fail")
        cursor=conn.cursor()
        params1 = {'fname':fname,'num':number}
        cursor.execute(que,params1)
        rows=cursor.fetchall()
        print(rows)
        for row in rows:
            count=row[0]
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
        print( "Connection closed")
    if(count>=1):
        print (count)
        print("Entry exist")
        return True
    else:
        print (count)
        print("No Entry found ")
        return False

    

    





    



