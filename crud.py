import mysql.connector

#connect to the database server
conn = None
mycursor = None
try :
    conn = mysql.connector.connect(
    host='127.0.0.1',
    user ='root',
    password = '',
    database='indigo'
     
    )
    mycursor = conn.cursor()
    print('Connection established')
except mysql.connector.errors.InterfaceError as err:
    print('Connection error')
    print(err)
    exit()



#create a database on the db server
#mycursor.execute("CREATE DATABASE indigo_new")
#conn.commit()

#create a table
#airport -> airport_id|code|name|city
#mycursor.execute(""" CREATE TABLE airport(
               #  airport_id INTEGER PRIMARY KEY,
                # CODE VARCHAR(10) NOT NULL,
               #  city VARCHAR(50) NOT NULL,
                # name VARCHAR(255) NOT NULL) """)
#conn.commit()
#insert data to the table
#mycursor.execute(""" INSERT INTO airport VALUES 
                 #(1,'DEL' , 'New Delhi', 'IGIA'),
                 #(2, 'CCU', 'Kolkata', 'NSCA'),
                 #(3, 'BOM','Mumbai', 'CSMA')
            # """)
#conn.commit()
#search/Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id >1")
data = mycursor.fetchall()
print(data)
for i in data:
    print(i[3])
    #update
    mycursor.execute(""" UPDATE airport
                     SET city = 'Bombay',
                        name = 'CSMA' 
                     WHERE airport_id = 3 """)
    conn.commit()
mycursor.execute("SELECT * FROM airport ")
data = mycursor.fetchall()
print(data)
#DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id =3")
conn.commit()
# mycursor.execute("SELECT * FROM airport ")
# data = mycursor.fetchall()
# print(data)

