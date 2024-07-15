import psycopg2
from dotenv import load_dotenv
import os
from connect import connect
from config import load_config

'''
# Load in the environmental variables
load_dotenv()

# Fetch the database variables
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')
'''

# Load the database configuration (user, pass, db)
config = load_config()

# Connect to your database
conn = connect(config)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
#cur.execute("SELECT schema_name FROM information_schema.schemata")
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema=\'nolestestschema\'")
#cur.execute("SELECT table_name FROM information_schema.tables")
#cur.execute("SELECT vendor_id FROM vendors")

# Retrieve all the rows from the cursor
tables = cur.fetchall()

# Print the names of the tables
for table in tables:
    print(table[0])

# Close the communication with the database
cur.close()
conn.close()
