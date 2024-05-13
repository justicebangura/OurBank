import os
import json
import logging
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates
import yfinance as yf
from pymongo import MongoClient


# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
def load_env():
    success = load_dotenv()
    if success:
        logging.info("Environment variables loaded successfully.")
    else:
        logging.error("Failed to load environment variables.")
    return success

load_env()

# Connect to MongoDB
def connect_mongodb():
    try:
        client = MongoClient(os.getenv("MONGODB_URI"))
        db = client["Crypto"]
        logging.info("Connected to MongoDB successfully.")
        return db
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        raise

db = connect_mongodb()

def store_user_account_info(username, email, hashed_password, account_balance):
    try:
        db.user_accounts.insert_one({
            "username": username,
            "email": email,
            "hashed_password": hashed_password,  # Ensure the password is properly hashed
            "account_balance": account_balance
        })
        logging.info("User account information stored securely in the database.")
    except Exception as e:
        logging.error(f"Failed to store user account information: {e}")
        raise

# Connect to Ganache
def connect_ganache():
    w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
    if not w3.is_connected():
        logging.error("Failed to connect to Ganache.")
        raise ConnectionError("Connection failed.")
    logging.info("Connected to Ganache successfully.")
    return w3

# Connect to Sepolia
def connect_sepolia():
    w3 = Web3(Web3.HTTPProvider(os.getenv("SEPOLIA_URL")))
    if not w3.is_connected():
        logging.error("Failed to connect to Sepolia.")
        raise ConnectionError("Connection failed.")
    logging.info("Connected to Sepolia successfully.")
    return w3

# Load Ethereum contract
def load_contract(w3, abi_path, contract_address):
    with open(Path(abi_path)) as f:
        contract_abi = json.load(f)
    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    logging.info(f"Contract loaded at address {contract_address}")
    return contract

# Retrieve Ethereum exchange information
def eth_exchange_info(contract):
    conversion_rate = contract.functions.getEthPrice().call() / 1e8
    logging.info(f"Current Ethereum exchange rate: {conversion_rate:.2f} USD/ETH")
    return conversion_rate

# Convert Ethereum to other currencies
def convert_eth_to_other_currency(eth_amount, conversion_rate, currency):
    c = CurrencyRates()
    usd_value = conversion_rate * eth_amount
    converted_value = c.convert("USD", currency, usd_value)
    logging.info(f"Converted {eth_amount} ETH to {converted_value:.2f} {currency}")
    return converted_value

# Retrieve stock information with additional data
def stock_info(stock_symbol):
    stock_symbol = stock_symbol.upper()
    data = yf.Ticker(stock_symbol)
    price_data = data.history(period="1d", interval="1m")["Close"].iloc[-1]
    logging.info(f"Current price for {stock_symbol}: ${price_data:.2f}")
    return price_data

# Transfer Ethereum with enhanced error handling
def transfer_eth(w3, from_account, to_account, amount):
    tx = {
        "to": Web3.to_checksum_address(to_account),
        "from": from_account,
        "value": w3.to_wei(amount, "ether"),
        "gas": 21000,
        "gasPrice": w3.to_wei("20", "gwei"),
    }
    try:
        tx_hash = w3.eth.send_transaction(tx)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        logging.info(f"Transaction successful with hash: {tx_hash.hex()}")
        return receipt
    except Exception as e:
        logging.error(f"Transaction failed: {e}")
        raise

# Additional utility function to get account balance
def get_crypto_balance(w3, account_address):
    balance = w3.eth.get_balance(account_address) / 1e18
    logging.info(f"Balance for account {account_address}: {balance:.2f} ETH")
    return balance
