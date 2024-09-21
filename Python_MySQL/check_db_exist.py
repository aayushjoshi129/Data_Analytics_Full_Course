import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database='mydatabase'
)

mycursor = mydb.cursor()

# SHOW DATABASES
'''
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''
  


# CREATE TABLE
''' 
mycursor.execute("CREATE TABLE CUSTOMERS (NAME VARCHAR(255), ADDRESS VARCHAR(255));") 
'''

'''
mycursor.execute("ALTER TABLE CUSTOMERS ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY;")
'''

# INSERT DATA
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
'''

# COMMIT COMMAND
'''
mydb.commit()  # mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
'''

# print(mycursor.rowcount, "record inserted.")


# INSERT MORE THAN 1 RECORD - DATA

'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "rows was inserted.")
'''


# SELECT COMMAND
'''
mycursor.execute("SELECT * from customers;")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
'''


# mycursor.execute("CREATE TABLE USERS (ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255), FAV VARCHAR(255))")
# mycursor.execute("INSERT INTO USERS VALUES (1, 'John',  154),(2, 'Peter',  154),(3, 'Amy',  155),(4, 'Hannah', 156),(5, 'Michael', 157)")
# mydb.commit()

# mycursor.execute("CREATE TABLE PRODUCTS (ID VARCHAR(255), NAME VARCHAR(255))")

# mycursor.execute("INSERT INTO PRODUCTS VALUES (  154,  'Chocolate Heaven' ),(  155, 'Tasty Lemons'),(  156, 'Vanilla Dreams')")
# mydb.commit()

'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

'''

'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

'''

'''
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
  
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
'''

