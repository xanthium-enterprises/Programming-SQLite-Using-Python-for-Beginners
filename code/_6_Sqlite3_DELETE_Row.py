#deleting a row using Python and SQLite 

import sqlite3

timestamp_to_delete = 1746705380  # time stamp of the first row

delete_sql_query    = "DELETE FROM data_logger WHERE TimeStamp = ?"

with sqlite3.connect("datalogger.sqlite") as connnection_object:
    cursor_object = connnection_object.cursor()
    
    
    cursor_object.execute(delete_sql_query, (timestamp_to_delete,))
    
    connnection_object.commit()

    if cursor_object.rowcount > 0:
        print(f"{cursor_object.rowcount} row(s) deleted.")
    else:
        print("No row found with that timestamp.")
