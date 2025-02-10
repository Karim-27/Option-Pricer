import math
import numpy
from scipy.stats import norm
import tkinter as tk
from tkinter import messagebox

#Calculating d1 and d2:
def calculate_d1_d2(stock_price, strike_price, interest_rate, time_maturity, volatility):
    d1 = (math.log(stock_price/strike_price) + ((interest_rate + ((volatility**2)/2)) * time_maturity)) / (volatility * (time_maturity**0.5))       
    d2 = d1 - (volatility * (time_maturity**0.5))

    return d1, d2

#Call Option:
def call_option_price(stock_price, strike_price, interest_rate, time_maturity, volatility):
    d1, d2 = calculate_d1_d2(stock_price, strike_price, interest_rate, time_maturity, volatility)
    call_price = (stock_price * norm.cdf(d1)) - (strike_price * (math.e**(-1 * interest_rate * time_maturity)) * norm.cdf(d2))
    
    return round(call_price, 2)

#Put Option:
def put_option_price(stock_price, strike_price, interest_rate, time_maturity, volatility):
    d1, d2 = calculate_d1_d2(stock_price, strike_price, interest_rate, time_maturity, volatility)
    put_price = (strike_price * (math.e**(-1 * interest_rate * time_maturity)) * norm.cdf(-d2)) - (stock_price * norm.cdf(-d1))
    
    return round(put_price, 2)

#Validating Inputs:
def valid_inputs(stock_price, strike_price, interest_rate, time_maturity, volatility):
    if stock_price <= 0:
        return "Stock price must be positive"
    elif strike_price <= 0:
        return "Strike price must be positive"
    elif interest_rate <= 0:
        return "Interest rate must be positive"
    elif time_maturity <= 0:
        return "Time to maturity must be positive"
    elif volatility <= 0:
        return "Volatility must be positive"
    else:
        return None

def calculate_option_prices():
    try:
        stock_price = float(stock_price_entry.get())
        strike_price = float(strike_price_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100
        time_maturity = float(time_maturity_entry.get())
        volatility = float(volatility_entry.get()) / 100
        
        error_message = valid_inputs(stock_price, strike_price, interest_rate, time_maturity, volatility)

        if error_message:
            messagebox.showerror("Input Error", error_message)
            
        #Calculate Option Prices
        call_price = call_option_price(stock_price, strike_price, interest_rate, time_maturity, volatility)
        put_price = put_option_price(stock_price, strike_price, interest_rate, time_maturity, volatility)
    
        #Display The Results
        call_price_label.config(text=f"Call Option Price: ${call_price}")
        put_price_label.config(text=f"Put Option Price: ${put_price}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please input a number")



#GUI
#Setting up the main window
root = tk.Tk()
root.title("Black Scholes Pricing Model")
root.geometry('450x450')

#Labels and Entries for Inputs
inputs = [
    ("Stock Price: ", "stock_price_entry"),
    ("Strike Price: ", "strike_price_entry"),
    ("Risk-Free Interest Rate (%): ", "interest_rate_entry"),
    ("Time to Maturity (Years): ", "time_maturity_entry"),
    ("Volatility (%): ", "volatility_entry"),
]

for label_text, entry_name in inputs:
    label = tk.Label(root, text=label_text)
    label.pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(pady=5)
    globals()[entry_name] = entry
    

#Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_option_prices)
calculate_button.pack(pady=10)

#Displaying Results
call_price_label = tk.Label(root, text="Call Option Price: $0.00")
call_price_label.pack(pady=5)

put_price_label = tk.Label(root, text="Put Option Price: $0.00")
put_price_label.pack(pady=5)

root.mainloop()



