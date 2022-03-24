import mysql.connector

#  to create Movie database
# conn = mysql.connector.connect(
#     host='localhost', username='root', password='New@1password')
# my_cursor = conn.cursor()  # create a cursor object

# query = 'CREATE DATABASE MovieDatabase;'
# my_cursor.execute(query)

# conn.commit()
# conn.close()

# connecting to mysql database MovieDatabase
conn = mysql.connector.connect(
    host='localhost', username='root', password='New@1password', database='MovieDatabase')


#  creating a table Movies in the database
# query = '''CREATE TABLE Movies(
#            name VARCHAR(255) NOT NULL,
#            leadActor VARCHAR(50) NOT NULL,
#            actress VARCHAR(50) NOT NULL,
#            releaseYear INT NOT NULL,
#            director VARCHAR(50) NOT NULL);
#  '''
my_cursor = conn.cursor()  # create a cursor object
# my_cursor.execute(query)
# conn.commit()

# inserting data  into database table
# query = 'INSERT INTO Movies VALUES("The Lord of the Rings Triology","Elijha wood","Liv Tyler",2001,"Peter Jackson");'
# query = 'INSERT INTO Movies VALUES("Harry Potter Series","Daniel Radcliffe","Emma Watson",2001,"Chris Columbus");'
# query = 'INSERT INTO Movies VALUES("Avengers:Endgame","Robert Downey Jr.","Scarlett Johansson",2019,"Russo Brothers");'
# query = 'INSERT INTO Movies VALUES("Spider-man:Into the spider-verse","Jake Johnson","hailee Steinfeld",2018,"Peter Ramsey");'
# query = 'INSERT INTO Movies VALUES("Catch me if You can","Leonardo DiCaprio","Amy Adams",2002,"Steven Spielberg");'
query = 'INSERT INTO Movies VALUES("Kimi no na wa","Ryunosuke Kamiki","Mone Kamishiraishi",2016,"Makoto Shinkai");'


my_cursor.execute(query)
conn.commit()


# reading data from database table
query = 'SELECT * FROM Movies;'
my_cursor.execute(query)
records = my_cursor.fetchall()
print(records)

query = 'SELECT * FROM Movies WHERE leadActor = "Daniel Radcliffe" AND releaseYear = 2001;'
my_cursor.execute(query)
records = my_cursor.fetchall()
print(records)

#  deleting data from database table
# query = 'DELETE FROM Movies WHERE name = "Catch me if You can";'
# my_cursor.execute(query)
# conn.commit()

conn.close()
