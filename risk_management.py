# Risk management and lot calculation (to be filled)

# risk_management.py

from config import *

def calculate_lot_size(price):
    # Calculate the lot size based on the risk per trade in BDT and SL percentage
    risk_amount = RISK_PER_TRADE_BDT
    sl_pips = price * SL_PERCENT / 100  # SL in pips based on the percentage
    lot_size = round(risk_amount / (sl_pips * 10), 2)  # Adjusting lot size formula
    return max(lot_size, 0.01)  # Minimum lot size is 0.01
