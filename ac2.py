### **1. Import Database**
"""

#Import file from your system


"""#### **2. Connect with SQLite Database**"""
# Connect to SQLite database
# Import necessary libraries
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

# Read SQL query for gettinb all the tables of databadr into a dataframe
# Here SELECT * means select all
import pandas as pd
tables = pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERR type='table';""",conn)
tables




