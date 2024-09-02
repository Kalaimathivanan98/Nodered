import pymysql

# Sample Data
sample_data = {
    "name": "Kalai",
    "age": 26,
    "number": "9150417503",
    "mailid": "kalaimathivanans@gmail.com",
    "country": "India"
}

try:
    # Establishing the connection to the MySQL database
    connection = pymysql.connect(
        host='database-1.cf0ckkk0msb6.us-east-1.rds.amazonaws.com',
        user='admin',  # Replace with your MySQL username
        password='lionelkalai@98',  # Replace with your MySQL password
        database='database-1-snapshot',  # Replace with your MySQL database name
        port=3306  # Port number should be specified here
    )

    # Creating a cursor object using the cursor() method
    with connection.cursor() as cursor:
        # SQL query to insert data into your table
        sql = "INSERT INTO your_table (name, age, number, mailid, country) VALUES (%s, %s, %s, %s, %s)"
        
        # Executing the query with the sample data
        cursor.execute(sql, (sample_data['name'], sample_data['age'], sample_data['number'], sample_data['mailid'], sample_data['country']))
    
    # Committing the transaction to save changes
    connection.commit()

    # Closing the connection
    connection.close()

    # Print success message
    print(f"Data's successfully injected into RDS MySQL database: {sample_data}")

except Exception as e:
    # Print error message if something goes wrong
    print(f"Failed to inject data into RDS MySQL: {str(e)}")
