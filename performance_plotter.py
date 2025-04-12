# Plot equity curve and performance (to be filled)

# performance_plotter.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_equity_curve(log_file='trade_log.csv'):
    df = pd.read_csv(log_file, header=None)
    df.columns = ['Date', 'Time', 'Day', 'Symbol', 'Direction', '% Profit', 'BDT Profit']
    df['Cumulative'] = df['BDT Profit'].cumsum()
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'].astype(str))
    plt.figure(figsize=(12, 6))
    plt.plot(df['DateTime'], df['Cumulative'], label='Equity Curve')
    plt.xlabel('DateTime')
    plt.ylabel('BDT Profit')
    plt.title('Equity Curve')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
