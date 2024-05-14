import bcrypt
import pymongo
import os
from dotenv import load_dotenv
import logging
import datetime

# Load environment variables
def load_env():
    success = load_dotenv()
    if success:
        logging.info("Environment variables loaded successfully.")
    else:
        logging.error("Failed to load environment variables.")
    return success

load_env()

client = pymongo.MongoClient(os.getenv("MONGO_CLIENT_URI"))

# Specify the database and collections
db = client["OurBank"]
users = db["users"]
transactions = db["transactions"]

# Function to create a new user account with hashed password
def open_new_account(username, raw_password):
    hashed_password = bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt())
    if users.find_one({"username": username}):
        raise ValueError("Username already exists!")
    users.insert_one({"username": username, "password": hashed_password, "balance": {}})
    return users.find_one({"username": username})

# Function to validate login credentials
def login_user(username, raw_password):
    user = users.find_one({"username": username})
    if user:
        stored_password = user["password"]
        return bcrypt.checkpw(raw_password.encode("utf-8"), stored_password)
    return False

def check_account_balance(username):
    user = users.find_one({"username": username})
    if user:
        return {"balance": user["balance"], "transactions": list(transactions.find())}
    raise ValueError("User not found")

# Function to deposit money into an account
def deposit_funds(username, amount, currency='USD'):
    user = users.find_one({"username": username})
    if user:
        if currency in user['balance']:
            users.update_one({"username": username}, {"$inc": {"balance." + currency: amount}})
        else:
            users.update_one({"username": username}, {"$set": {"balance." + currency: amount}})
        transaction = {"type": "deposit", "username": username, "amount": amount, "currency": currency, "timestamp": datetime.datetime.now().replace(microsecond=0)}
        transactions.insert_one(transaction)
        return users.find_one({"username": username})["balance"]
    raise ValueError("User not found")

# Function to withdraw money from an account
def withdraw_funds(username, amount, currency='USD'):
    user = users.find_one({"username": username})
    if user:
        if user["balance"].get(currency, 0) < amount:
            raise ValueError("Insufficient balance")
        users.update_one({"username": username}, {"$inc": {"balance." + currency: -amount}})
        transaction = {"type": "withdrawal", "username": username, "amount": amount, "currency": currency, "timestamp": datetime.datetime.now().replace(microsecond=0)}
        transactions.insert_one(transaction)
        return users.find_one({"username": username})["balance"]
    raise ValueError("User not found")

# Function to transfer money between accounts
def transfer_funds(sender, receiver, amount):
    sender_data = users.find_one({"username": sender})
    receiver_data = users.find_one({"username": receiver})
    if sender_data and receiver_data:
        if sender_data["balance"].get("USD", 0) < amount:
            raise ValueError("Insufficient balance")
        users.update_one({"username": sender}, {"$inc": {"balance.USD": -amount}})
        users.update_one({"username": receiver}, {"$inc": {"balance.USD": amount}})
        transaction = {
            "type": "transfer",
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": datetime.datetime.now().replace(microsecond=0),
        }
        transactions.insert_one(transaction)
        return users.find_one({"username": sender})["balance"], users.find_one({"username": receiver})["balance"]
    raise ValueError("One or both users not found")

#add store transaction history  
