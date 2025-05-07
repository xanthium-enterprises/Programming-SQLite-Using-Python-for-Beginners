#adding some data into sqlite database

import sqlite3
import time

# Sample data
temp1 = 25.3
temp2 = 34.6
temp3 = 24.8
ip_address = '192.168.0.101'
timestamp = int(time.time())  # current Unix time

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

    cursor_object.execute(insert_data_sql_query, (temp1, temp2, temp3, ip_address, timestamp))

    print("Data inserted successfully.")
