#sample_prog_snowflake.py
import snowflake.connector

# Replace these variables with your actual credentials
# https://obb68612.us-east-1.snowflakecomputing.com
user = 'pravin082024'
password = 'Orange@082024'
account = 'jkphxak-uvb85840'
database = 'SNOWFLAKE_SAMPLE_DATA'
schema = 'TPCH_SF1'

# Establish a connection to Snowflake
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    database=database,
    schema=schema
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