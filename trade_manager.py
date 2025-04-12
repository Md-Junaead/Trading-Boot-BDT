# Trade execution and trailing stop logic (to be filled)

# trade_manager.py

import MetaTrader5 as mt5
from config import *
from datetime import datetime

def place_order(symbol, action, lot, sl_price, tp_price):
    order_type = mt5.ORDER_TYPE_BUY if action == 'buy' else mt5.ORDER_TYPE_SELL
    price = mt5.symbol_info_tick(symbol).ask if action == 'buy' else mt5.symbol_info_tick(symbol).bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl_price,
        "tp": tp_price,
        "deviation": 10,
        "magic": 234000,
        "comment": "AutoTrade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    return result
