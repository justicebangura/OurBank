import bcrypt
import datetime

# Dictionary to store user data
users = {}
 # List to store all transactions
transactions = []

# Function to create a new user account with hashed password
def open_account(username, raw_password):
    hashed_password = bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt())
    if username in users:
        raise ValueError("Username already exists!")
    users[username] = {"password": hashed_password, "balance": 0}
    return users[username]

# Function to validate login credentials
def login(username, raw_password):
    if username in users:
        stored_password = users[username]["password"]
        return bcrypt.checkpw(raw_password.encode("utf-8"), stored_password)
    return False

# Function to get account details
def account_balance(username):
    if username in users:
        return {"balance": users[username]["balance"], "transactions": transactions}
    raise ValueError("User not found")

# Function to deposit money into an account
def deposit(username, amount):
    if username not in users:
        raise ValueError("User not found")
    users[username]["balance"] += amount
    transaction = {"type": "deposit", "username": username, "amount": amount, "timestamp": datetime.datetime.now()}
    transactions.append(transaction)
    return users[username]["balance"]

# Function to withdraw money from an account
def withdraw(username, amount):
    if username not in users:
        raise ValueError("User not found")
    if users[username]["balance"] < amount:
        raise ValueError("Insufficient balance")
    users[username]["balance"] -= amount
    transaction = {"type": "withdrawal", "username": username, "amount": amount, "timestamp": datetime.datetime.now()}
    transactions.append(transaction)
    return users[username]["balance"]

# Function to transfer money between accounts
def transfer(sender, receiver, amount):
    if sender not in users or receiver not in users:
        raise ValueError("One or both users not found")
    if users[sender]["balance"] < amount:
        raise ValueError("Insufficient balance")
    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount
    transaction = {
        "type": "transfer",
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "timestamp": datetime.datetime.now(),
    }
    transactions.append(transaction)
    return users[sender]["balance"], users[receiver]["balance"]