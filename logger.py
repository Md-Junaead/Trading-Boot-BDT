# Logs all trades to CSV (to be filled)

# logger.py

import csv
from datetime import datetime

LOG_FILE = "trade_log.csv"

def log_trade(symbol, direction, profit_pct, profit_bdt):
    # Log each trade's details in a CSV file
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        now = datetime.now()
        day_name = now.strftime('%A')
        writer.writerow([now.date(), now.time(), day_name, symbol, direction, profit_pct, profit_bdt])
