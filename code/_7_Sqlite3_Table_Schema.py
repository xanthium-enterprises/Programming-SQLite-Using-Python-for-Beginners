#Retrieve the Schema of a Table Using Python

import sqlite3

# Connect to the SQLite database
with sqlite3.connect("datalogger.sqlite") as connnection_object:
    cursor_object = connnection_object.cursor()

    # Query the schema of a specific table (e.g., 'data_logger')
    cursor_object.execute("""
        SELECT sql FROM sqlite_master 
        WHERE type='table' AND name='data_logger'
    """)
    
    result = cursor_object.fetchone()

    if result:
        print("Schema for 'data_logger':\n")
        print(result[0])  # This is the CREATE TABLE statement
        
    else:
        print("Table 'data_logger' not found.")
