import os
import json
import logging  # For enhanced logging
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates
import yfinance as yf
from datetime import datetime  # For timestamp handling

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
    usd_value = conversion_rate * eth_amount
    converted_value = currency_converter(currency, usd_value)
    logging.info(f"Converted {eth_amount} ETH to {converted_value:.2f} {currency}")
    return converted_value

# Retrieve stock information with additional data
def stock_info(conversion_rate, stock_symbol):
    stock_symbol = stock_symbol.upper()
    data = yf.Ticker(stock_symbol)
    price_data = data.history(period="1d", interval="1m")["Close"].iloc[-1]
    price_in_eth = price_data / conversion_rate
    logging.info(f"Current price for {stock_symbol}: ${price_data:.2f}")
    return price_data, price_in_eth

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
def get_account_balance(w3, account_address):
    balance = w3.eth.get_balance(account_address) / 1e18
    logging.info(f"Balance for account {account_address}: {balance:.2f} ETH")
    return balance

def currency_converter(currency, price):
  if currency == 'USD':
    return price
  currency_pair = f'USD{currency}=X'

  currency_data = yf.Ticker(currency_pair)
  exchange_rate = currency_data.history(period = '1d', interval = '1m')["Close"].iloc[-1]
  return price * exchange_rate




