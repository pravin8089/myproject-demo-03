import cx_Oracle
import json

# Load Oracle configuration from JSON file
with open('../configs/db_oracle_config.json') as f:
    config = json.load(f)

# Establish a connection
connection = cx_Oracle.connect(
    user=config['user'],
    password=config['password'],
    dsn=config['dsn']
)

# Create a cursor
cursor = connection.cursor()

# Execute a query
cursor.execute("""
    SELECT count (1) cnt
    FROM employees
""")

# Fetch and print the results
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
