# Strategy logic (to be filled)
# strategy.py

import pandas as pd
import MetaTrader5 as mt5

def get_data(symbol, timeframe, bars=100):
    tf = getattr(mt5, f'TIMEFRAME_{timeframe}')
    rates = mt5.copy_rates_from_pos(symbol, tf, 0, bars)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def calculate_indicators(df):
    # Calculate RSI and Bollinger Bands for the strategy
    df['rsi'] = df['close'].rolling(14).apply(lambda x: 100 - 100 / (1 + (x[-1] - x.mean()) / (x.std() + 1e-6)))
    df['ma20'] = df['close'].rolling(window=20).mean()
    df['stddev'] = df['close'].rolling(window=20).std()
    df['upper_bb'] = df['ma20'] + (df['stddev'] * 2)
    df['lower_bb'] = df['ma20'] - (df['stddev'] * 2)
    return df

def check_signal(df):
    if df is None or len(df) < 21:
        return None

    last = df.iloc[-1]
    if last['close'] < last['lower_bb'] and last['rsi'] < 30:
        return 'buy'
    elif last['close'] > last['upper_bb'] and last['rsi'] > 70:
        return 'sell'
    return None
