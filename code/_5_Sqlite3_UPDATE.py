#updating the SQLite table data using UPDATE

import sqlite3

# New data that will be used to update.
new_temp1 = 2900.5
new_temp2 = 3500.0
new_temp3 = 2800.7

timestamp_to_update = 1746599012  # time stamp of the first row 

update_data_sql_query = '''
                            UPDATE data_logger
                            SET Temp_Sensor1 = ?, Temp_Sensor2 = ?, Temp_Sensor3 = ?
                            WHERE TimeStamp = ?
                         '''

# Connect to database
with sqlite3.connect("datalogger.sqlite") as connnection_object:
    cursor_object = connnection_object.cursor()
    
   
    
    cursor_object.execute(update_data_sql_query, (new_temp1, new_temp2, new_temp3, timestamp_to_update))
    connnection_object.commit()

    if cursor_object.rowcount > 0:
        print("Row updated successfully.")
    else:
        print("No row found with the given timestamp.")
