import math
import numpy
from scipy.stats import norm
import tkinter as tk
from tkinter import messagebox


#Call Option:
def call_option_price(stock_price, strike_price, interest_rate, time_maturity,\
                      volatility):
    
    d1 = (math.log(stock_price/strike_price) + ((interest_rate + \
        ((volatility**2)/2)) * time_maturity)) / (volatility * \
                                                  (time_maturity**0.5))       
    d2 = d1 - (volatility * (time_maturity**0.5))
    
    c_norm_cdf_d1 = norm.cdf(d1)
    c_norm_cdf_d2 = norm.cdf(d2)
    
    call_price = (stock_price * c_norm_cdf_d1) - (strike_price * (math.e**(-1\
                    * interest_rate * time_maturity)) * c_norm_cdf_d2)
    
    return round(call_price, 2)

#Put Option:
def put_option_price(stock_price, strike_price, interest_rate, time_maturity,\
                     volatility):
    
    d1 = (math.log(stock_price/strike_price) + ((interest_rate + \
        ((volatility**2)/2)) * time_maturity)) / (volatility * \
                                                  (time_maturity**0.5))       
    d2 = d1 - (volatility * (time_maturity**0.5))
    
    p_norm_cdf_d1 = norm.cdf(-1 * d1)
    p_norm_cdf_d2 = norm.cdf(-1 * d2)
    
    put_price = (strike_price * (math.e**(-1 * interest_rate * time_maturity))\
                 * p_norm_cdf_d2) - (stock_price * p_norm_cdf_d1)
    
    return round(put_price, 2)


def calculate_option_prices():
    
    stock_price = float(stock_price_entry.get())
    strike_price = float(strike_price_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100
    time_maturity = float(time_maturity_entry.get())
    volatility = float(volatility_entry.get()) / 100
    
    # Check if inputs are valid
    if stock_price <= 0:
        messagebox.showerror("Input Error", "Stock price must be positive")
        return
    elif strike_price <= 0:
        messagebox.showerror("Input Error", "Strike price must be positive")
        return
    elif time_maturity <= 0:
        messagebox.showerror("Input Error", "Time to maturity must be positive")
        return
    elif volatility <= 0:
        messagebox.showerror("Input Error", "Volatility must be positive")
        return

    #Calculate Option Prices
    call_price = call_option_price(stock_price, strike_price, interest_rate, \
                    time_maturity, volatility)
    put_price = put_option_price(stock_price, strike_price, interest_rate, \
                    time_maturity, volatility)
    
    #Display The Results
    call_price_label.config(text=f"Call Option Price: ${call_price}")
    put_price_label.config(text=f"Put Option Price: ${put_price}")
    


#GUI
#Setting up the main window
root = tk.Tk()
root.title("Black Scholes Pricing Model")
root.geometry('450x450')

#Labels and Entries for Inputs
stock_price_label = tk.Label(root, text="Stock Price: ")
stock_price_label.pack(pady=5)
stock_price_entry = tk.Entry(root)
stock_price_entry.pack(pady=5)

strike_price_label = tk.Label(root, text="Strike Price:")
strike_price_label.pack(pady=5)
strike_price_entry = tk.Entry(root)
strike_price_entry.pack(pady=5)

interest_rate_label = tk.Label(root, text="Risk-Free Interest Rate (%):")
interest_rate_label.pack(pady=5)
interest_rate_entry = tk.Entry(root)
interest_rate_entry.pack(pady=5)

time_maturity_label = tk.Label(root, text="Time to Maturity (Years):")
time_maturity_label.pack(pady=5)
time_maturity_entry = tk.Entry(root)
time_maturity_entry.pack(pady=5)

volatility_label = tk.Label(root, text="Volatility (%):")
volatility_label.pack(pady=5)
volatility_entry = tk.Entry(root)
volatility_entry.pack(pady=5)

#Calculate Button
calculate_button = tk.Button(root, text="Calculate", \
                             command=calculate_option_prices)
calculate_button.pack(pady=10)

#Displaying Results
call_price_label = tk.Label(root, text="Call Option Price: $0.00")
call_price_label.pack(pady=5)

put_price_label = tk.Label(root, text="Put Option Price: $0.00")
put_price_label.pack(pady=5)

root.mainloop()



