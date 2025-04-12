# GUI for bot control (to be filled)

# gui.py

import tkinter as tk
import threading
from main import run_bot
from performance_plotter import plot_equity_curve

def start_bot():
    threading.Thread(target=run_bot).start()

def show_performance():
    plot_equity_curve()

def set_risk():
    risk = float(risk_entry.get())
    print(f"Risk set to: {risk} BDT")  # Update risk management based on user input

root = tk.Tk()
root.title("MT5 Trading Bot GUI")
root.geometry("300x200")

# Risk input
tk.Label(root, text="Risk per Trade (BDT)").pack(pady=10)
risk_entry = tk.Entry(root)
risk_entry.pack(pady=5)
risk_button = tk.Button(root, text="Set Risk", command=set_risk, height=2, width=20)
risk_button.pack(pady=10)

# Buttons for starting the bot and viewing performance
start_btn = tk.Button(root, text="Start Bot", command=start_bot, height=2, width=20, bg="green", fg="white")
start_btn.pack(pady=10)

plot_btn = tk.Button(root, text="Show Performance", command=show_performance, height=2, width=20)
plot_btn.pack(pady=10)

root.mainloop()
