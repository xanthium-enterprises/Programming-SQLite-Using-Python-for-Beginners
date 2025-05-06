#Python code to create a table in sqlite using STRICT option

import sqlite3

create_table_sql_query = '''

CREATE TABLE IF NOT EXISTS data_logger(
                                        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, --Primary Key 
                                        Temp_Sensor1 REAL,   -- Temperature values in Degrees like 34.67
                                        Temp_Sensor2 REAL,   -- Temperature values in Degrees
                                        Temp_Sensor3 REAL,   -- Temperature values in Degrees
                                        IP_Address   TEXT,   -- ip address like 192.168.1.1
                                        TimeStamp    INTEGER -- time in unix time
                                        
                                       ) STRICT;   -- Space before STRICT                                                   '''

connection_object = sqlite3.connect('datalogger.sqlite')  # Connect to a database (or create it if it doesn't exist)
cursor_object     = connection_object.cursor()            # Create a cursor object using the previous connection object

cursor_object.execute(create_table_sql_query)             # create the table
connection_object.commit()                                # commit the changes to the database
connection_object.close()                                 # close the connection


