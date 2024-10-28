import snowflake.connector
import json

# Load Snowflake configuration from JSON file
with open('../configs/db_snowflake_config.json') as f:
    config = json.load(f)

# Establish a connection to Snowflake
conn = snowflake.connector.connect(
    user=config['user'],
    password=config['password'],
    account=config['account'],
    database=config['database'],
    schema=config['schema']
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT count(1) FROM CUSTOMER")

# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()