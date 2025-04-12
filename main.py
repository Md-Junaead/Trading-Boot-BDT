# Main bot runner (to be filled)

# main.py

import MetaTrader5 as mt5
from config import *
from strategy import get_data, calculate_indicators, check_signal
from risk_management import calculate_lot_size
from trade_manager import place_order
from logger import log_trade

def run_bot():
    if not mt5.initialize():
        print("MT5 initialization failed")
        return

    df = get_data(SYMBOL, TIMEFRAME)
    df = calculate_indicators(df)
    signal = check_signal(df)

    if signal:
        price = df['close'].iloc[-1]
        lot = calculate_lot_size(price)
        sl = price * (1 - SL_PERCENT/100) if signal == 'buy' else price * (1 + SL_PERCENT/100)
        tp = price * (1 + TP_PERCENT/100) if signal == 'buy' else price * (1 - TP_PERCENT/100)
        result = place_order(SYMBOL, signal, lot, sl, tp)

        # Logging the trade details
        profit_pct = (result['profit'] / price) * 100 if 'profit' in result else 0
        profit_bdt = result['profit'] * price  # convert profit to BDT
        log_trade(SYMBOL, signal, profit_pct, profit_bdt)
        print(f"Trade Result: {result}")

    mt5.shutdown()
