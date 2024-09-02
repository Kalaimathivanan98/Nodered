import psycopg2

# Sample Data
sample_data = {
    "name": "Kalai",
    "age": 26,
    "number": "9150417503",
    "mailid": "kalaimathivanans@gmail.com",
    "country": "India"
}

try:
    connection = psycopg2.connect(
        dbname='yourdatabase',
        user='awsuser',
        password='password',
        host='your-redshift-endpoint',
        port='5439'
    )
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO your_table (name, age, number, mailid, country) VALUES (%s, %s, %s, %s, %s)", 
                       (sample_data['name'], sample_data['age'], sample_data['number'], sample_data['mailid'], sample_data['country']))
    connection.commit()
    connection.close()
    print(f"Data's successfully injected into Redshift database: {sample_data}")
except Exception as e:
    print(f"Failed to inject data into Redshift: {str(e)}")
