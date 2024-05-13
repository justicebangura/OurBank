import bcrypt
import pymongo
import os
from dotenv import load_dotenv
import logging

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
    existing_user = users.find_one({"username": username})
    if existing_user:
        raise ValueError("Username already exists!")
    users.insert_one({"username": username, "password": hashed_password, "balance": 0})
    return {"username": username, "password": hashed_password, "balance": 0}


# Function to validate login credentials
def login_user(username, raw_password):
    user = users.find_one({"username": username})
    if user:
        stored_password = user["password"]
        return bcrypt.checkpw(raw_password.encode("utf-8"), stored_password)
    return False

# Function to deposit money into an account
def deposit_funds(username, amount):
    user = users.find_one({"username": username})
    if not user:
        raise ValueError("User not found")
    new_balance = user["balance"] + amount
    users.update_one({"username": username}, {"$set": {"balance": new_balance}})
    return new_balance

# Function to withdraw money from an account
def withdraw_funds(username, amount):
    user = users.find_one({"username": username})
    if not user:
        raise ValueError("User not found")
    if user["balance"] < amount:
        raise ValueError("Insufficient balance")
    new_balance = user["balance"] - amount
    users.update_one({"username": username}, {"$set": {"balance": new_balance}})
    return new_balance

# Function to transfer money between accounts
def transfer_funds(sender, receiver, amount):
    sender_user = users.find_one({"username": sender})
    receiver_user = users.find_one({"username": receiver})
    if not sender_user or not receiver_user:
        raise ValueError("One or both users not found")
    if sender_user["balance"] < amount:
        raise ValueError("Insufficient balance")
    sender_new_balance = sender_user["balance"] - amount
    receiver_new_balance = receiver_user["balance"] + amount
    users.update_one({"username": sender}, {"$set": {"balance": sender_new_balance}})
    users.update_one({"username": receiver}, {"$set": {"balance": receiver_new_balance}})
    return sender_new_balance, receiver_new_balance

def get_account_balance(username):
    user = users.find_one({"username": username})
    if user:
        return user["balance"]
    else:
        raise ValueError("User not found")

