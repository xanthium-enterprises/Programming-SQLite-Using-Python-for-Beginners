#Reading data from SQLite database using fetchall

import sqlite3

# Connect to the database
with sqlite3.connect('datalogger.sqlite') as connection_object:
    cursor_object  = connection_object.cursor()
    
    cursor_object.execute('SELECT * FROM data_logger') #Execute a SELECT query
    
    rows = cursor_object.fetchall() #Fetch all rows
    
    # Print each row
    for row in rows:
        print(row)
