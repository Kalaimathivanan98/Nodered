from pymongo import MongoClient

# Sample Data
sample_data = {
    "name": "Kalai",
    "age": 26,
    "number": "9150417503",
    "mailid": "kalaimathivanans@gmail.com",
    "country": "India"
}

try:
    # Update this path to the actual location of your global-bundle.pem file
    client = MongoClient(
        'mongodb://admin01:admin2000@docdb-2024-08-24-08-22-17.cf0ckkk0msb6.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false'
    )
    db = client['test']
    collection = db['test10']
    collection.insert_one(sample_data)
    print(f"Data's successfully injected into DocumentDB database: {sample_data}")
except Exception as e:
    print(f"Failed to inject data into DocumentDB: {str(e)}")
