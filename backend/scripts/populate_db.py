from faker import Faker
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection string
db = client["your_database"]  # Replace "your_database" with your MongoDB database name

# Initialize Faker
fake = Faker()

# Insert fake data into MongoDB collection
items_collection = db["items"]
for _ in range(10):  # Insert 10 items as an example
    item = {
        "item_name": fake.word(),
        "description": fake.sentence(),
        "price": fake.random_number(digits=2)
    }
    items_collection.insert_one(item)

# Close the MongoDB connection
client.close()