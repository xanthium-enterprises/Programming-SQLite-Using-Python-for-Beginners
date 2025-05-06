import sqlite3

print("SQLite version        :", sqlite3.sqlite_version)  # version of the sqlite
print("sqlite3 module version:", sqlite3.version)         # version of the module library 

conn = sqlite3.connect('mydatabase.db') # create a connection object

conn.close()