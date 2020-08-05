# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:13:32 2020

@author: shivang dargar(only for databse connection),sandeep makwana
@typed by sandeep makwana
"""
import pyinputplus as pyip # input 
import mysql
import mysql.connector
from mysql.connector import Error
def dbconn():
    try:
        mydb=mysql.connector.connect(
                host="localhost",
                #port=3306,    port no is nessasary
                db="electronics",
                user="root",
                password="sandeepmakwana@123",   # if password is not avilable than password ="",
                )
        if mydb.is_connected():  # for using connection ...
            

            #-------------------------------------------------------------------------------------------------------------
            
            #for check the information of MYsql 
            
            #db_Info = mydb.get_server_info()
            #print("Connected to MYSQL server version ", db_Info)
            
            #----------------------------------------------------------------------------------------------------------
            
            
            
            
            cursor = mydb.cursor()          # use cursor to ecteract the query like adding , insert Other
            
            print("connected successful")
            #----------------------------------------------------------------------------------------------------------------
            '''
            # condition 1:    =>(create a DataBase)<=
            
                        
            cursor.execute("CREATE DATABASE electronics")
            mydb.commit()
            print("Data Bases created ")
            '''
            #-----------------------------------------------------------------------------------------------------------------
            
            
            '''
            # condition 2:    =>(creater the tabel)<=
                      
            
            cursor.execute("CREATE TABLE products(pid integer PRIMARY KEY,pame varchar(50) NOT NULL,price double NOT NULL, copany varchar(30) NOT NULL)")
            mydb.commit()
            print("table is created ")
            '''
            
            #-------------------------------------------------------------------------------------------------------------------------------------------------------
            
            
            '''
            
            #condition 3: =>(insert oneline data in the table)<=
            
            cursor.execute("INSERT INTO mytab VALUES(105, 'Vinod', 34000, 'Jabalpur')")
            mydb.commit()
            print ("record secces full added")
            
            '''
            
            #-----------------------------------------------------------------------------------------------------------------------------------------------------------
            
            '''
            #condition 4: =>(insert  user input data in the table)<=
            
            pid = pyip.inputInt("Enter the produt Id:")
            pn = pyip.inputStr("Enter the Product Name :")
            pr = pyip.inputFloat("Enter the Product Price :")
            com = pyip.inputStr("Enter the Company Name : ")
            
            cursor.execute("INSERT INTO products(pid, pame, price, copany) VALUES ('"+str(pid)+"', '"+pn+"', '"+str(pr)+"', '"+com+"')")
            mydb.commit()
            print('record is added')
            '''
            
            
            #-----------------------------------------------------------------------------------------------------------------------------------------
            
            """
            #condition 5: =>(insert  user many line data in the table)<=
            
            
            query = "INSERT INTO products(pid, pame, price, copany) VALUES (%s,%s,%s,%s)"
            data = [(101,"Mouse",250.00, "iBall"),
                    (102, "KeyBoard", 250.00, "iBAll"),
                    (103, "LCD", 50000.00, "Acer"),
                    (104, "Pen Drive", 300, "Kingston"),
                    ]
            cursor.executemany(query, data)
            mydb.commit()
            print (records are added in the table)
            #print ("Products Inserted Successfully")
            
            """
            
            
            #--------------------------------------------------------------------------------------------------------------------------------------------
            
            """
            #condition 6: =>(update data of the table)<=
            
            
            pid = pyip.inputInt("Enter the produt Id:")
            pn = pyip.inputStr("Enter the Product Name :")
            pr = pyip.inputFloat("Enter the Product Price :")
            com = pyip.inputStr("Enter the Company Name : ")
            query = "UPDATE products SET pame='"+pn+"', price= '"+str(pr)+"', copany='"+com+"' WHERE pid='"+str(pid)+"'"
            cursor.execute(query)
            
            mydb.commit()
            print ("data is updated")
            
            """
            #-----------------------------------------------------------------------------------------------------------------------------------------------
            
            """
             #condition 7: =>(Delete tdata in the table)<= with using condition
             
            pid = pyip.inputInt("Enter the produt Id:")
            query = "DELETE FROM products WHERE pid='"+str(pid)+"'" 
            cursor.execute(query)
            mydb.commit()
            print("Delet secusess full !")
            """
            
            
            #-----------------------------------------------------------------------------------------------------------------------------------------------
            
            """
            #condition 8: =>(full table is deleted )<=
            
            query = "TRUNCATE TABLE products" 
            cursor.execute(query)
            mydb.commit()
            print("Deleted full table secusess full !")
            
            
            """
            
            
            #------------------------------------------------------------------------------------------------------------------------------------------------
            #------------------------------------------------------------------------------------------------------------------------------------------------
            '''             DATABASE to PYTHON consule (data show in data base)            '''
            #------------------------------------------------------------------------------------------------------------------------------------------------
            #------------------------------------------------------------------------------------------------------------------------------------------------
            
            '''
            
            #condition 9: =>(showing all data in  the table)<= whith using conditions
            query = "SELECT * FROM products"
            cursor.execute(query)
            rec = cursor.fetchall()
            for i in rec:
                print("Product id :", i[0])
                print("Product name :", i[1])
                print("Product price : ", i[2])
                print("Product company", i[3])
                print("******************************")
            print("NO of rows in the table : ", cursor.rowcount) 
            
            '''

            #---------------------------------------------------------------------------------------------------------------------------------------------------
            
            
            '''
            #condition 10: =>(showing one line the table)<= whith using conditions
            
            
            
            
            pn= input("inter the product name of this table : ")
            query = "SELECT * FROM products WHERE pame='"+pn+"'"
            cursor.execute(query)
            rec = cursor.fetchone()
            print(rec)
            #please mydib.commit() will be commants 
            
            '''
            
            
        else: 
            print("connection is faild")
    except Error as e:
        print("raise connceted",e)
    finally:
        if mydb.is_connected():
            mydb.close()
            print("connection closed")
dbconn()

