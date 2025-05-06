#Python code to create a table in sqlite using STRICT option
#using context manager 'with'

import sqlite3

create_table_sql_query = '''

CREATE TABLE IF NOT EXISTS data_logger(
                                        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, --Primary Key 
                                        Temp_Sensor1 REAL,   -- Temperature values in Degrees like 34.67
                                        Temp_Sensor2 REAL,   -- Temperature values in Degrees
                                        Temp_Sensor3 REAL,   -- Temperature values in Degrees
                                        IP_Address   TEXT,   -- ip address like 192.168.1.1
                                        TimeStamp    INTEGER -- time in unix time
                                        
                                       ) STRICT;  -- Space before STRICT                                                     '''

with sqlite3.connect('datalogger.sqlite') as connection_object : # Connect to a database (or create it if it doesn't exist)
    cursor_object     = connection_object.cursor()                # Create a cursor object using the previous connection object
    cursor_object.execute(create_table_sql_query)                 # create the table
   
    # connection_object.commit()
    # You don’t need connection_object.commit() inside a with block
    # SQLite auto-commits when the with block exits without errors.
    # But including it explicitly doesn’t harm.


                                                                 



