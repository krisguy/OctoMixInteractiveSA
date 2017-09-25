''' This script creates a db and table for auth assist '''
# Imports the sqlite3 library
import sqlite3

# Creates a connection to the database or creates a database
# If it does not exist then it will make one automatically
CONN = sqlite3.connect('example.db3')

# Creates a table called account with the rows 'id' and 'data'
CONN.execute('''CREATE TABLE account
             (id text, data)''')

# Creates a list of information that we will enter into the database
DATA = [('access_token', None),
        ('refresh_token', None),
        ('expires_in', None),
        ('token_type', None)]

# Add the information from DATA to the database
CONN.executemany("INSERT INTO account VALUES (?,?)", DATA)

# Commit the changes made to the database
CONN.commit()
