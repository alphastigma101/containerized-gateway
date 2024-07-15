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
with conn.cursor() as cur:

    # Execute a create-table query
    cur.execute('CREATE SCHEMA nolesTestSchema')
    #cur.execute('CREATE SCHEMA AUTHORIZATION nole2;')
    #cur.execute('SELECT schema_name FROM information_schema.schemata;')
    #cur.execute('SELECT datname FROM pg_database;')

conn.commit()
conn.close()
