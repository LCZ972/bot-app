import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
WALLET_1 = os.getenv("WALLET_1")
WALLET_2 = os.getenv("WALLET_2")
YOUR_WALLET = os.getenv("YOUR_WALLET")
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

def get_recent_transactions(wallet_address):
    url = f"https://api.helius.xyz/v0/addresses/{wallet_address}/transactions?api-key={HELIUS_API_KEY}&limit=5"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur API Helius : {response.status_code}")
        print(response.text)  # affiche l'erreur exacte
        return []

def is_token_swap(tx):
    return "swapEvent" in tx.get("events", {})

def analyze_wallet(wallet_address):
    transactions = get_recent_transactions(wallet_address)
    for tx in transactions:
        if is_token_swap(tx):
            print(f"\n💰 Swap détecté sur {wallet_address}")
            print(f"↪️ Signature : {tx.get('signature')}")
            print(f"📅 Date : {tx.get('timestamp')}")
            print(f"➡️ Lien : https://solscan.io/tx/{tx.get('signature')}")

print("🚀 Bot démarré, en attente de swaps...")
while True:
    analyze_wallet(WALLET_1)
    analyze_wallet(WALLET_2)
    time.sleep(10)