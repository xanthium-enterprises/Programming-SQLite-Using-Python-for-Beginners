#adding a lot of data into table using executemany()

import sqlite3
import time

# Sample data list

data_list = [ (25.3, 34.6, 24.8, '192.168.0.101', int( time.time() ) ),
              (26.1, 35.2, 25.4, '192.168.0.102', int( time.time() ) ),
              (24.9, 33.8, 23.7, '192.168.0.103', int( time.time() ) )
             ]





insert_data_sql_query = '''
 
           INSERT INTO data_logger (Temp_Sensor1,
                                    Temp_Sensor2,
                                    Temp_Sensor3,
                                    IP_Address,
                                    TimeStamp)
           VALUES (?, ?, ?, ?, ?)
    '''


# Connect and insert data
with sqlite3.connect('datalogger.sqlite') as connection_object:
    cursor_object  = connection_object.cursor()

    cursor_object.executemany(insert_data_sql_query,data_list)

    print("Data inserted successfully.")

