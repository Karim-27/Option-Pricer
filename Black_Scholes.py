import tkinter as tk
from tkinter import messagebox
from Calculations import call_option_price, put_option_price

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

def open_black_scholes():
    black_scholes = tk.Toplevel()
    black_scholes.title("Black-Scholes Calculator")
    black_scholes.geometry("450x450")

    inputs = [
    ("Stock Price: ", "stock_price_entry"),
    ("Strike Price: ", "strike_price_entry"),
    ("Risk-Free Interest Rate (%): ", "interest_rate_entry"),
    ("Time to Maturity (Years): ", "time_maturity_entry"),
    ("Volatility (%): ", "volatility_entry"),]

    #Dictionary to store entries
    entry_fields = {}

    for label_text, entry_name in inputs:
        label = tk.Label(black_scholes, text=label_text)
        label.pack(pady=5)
        entry = tk.Entry(black_scholes)
        entry.pack(pady=5)
        entry_fields[entry_name] = entry #Store in dictionary

    call_price_label = tk.Label(black_scholes, text="Call Option Price: $0.00")
    call_price_label.pack(pady=5)

    put_price_label = tk.Label(black_scholes, text="Put Option Price: $0.00")
    put_price_label.pack(pady=5)

    def calculate_option_prices():
        try:
            stock_price = float(entry_fields["stock_price_entry"].get())
            strike_price = float(entry_fields["strike_price_entry"].get())
            interest_rate = float(entry_fields["interest_rate_entry"].get()) / 100
            time_maturity = float(entry_fields["time_maturity_entry"].get())
            volatility = float(entry_fields["volatility_entry"].get()) / 100
        
            error_message = valid_inputs(stock_price, strike_price, interest_rate, time_maturity, volatility)

            if error_message:
                messagebox.showerror("Input Error", error_message)
                return # Exits function if there's an error
            
            #Calculate Option Prices
            call_price = call_option_price(stock_price, strike_price, interest_rate, time_maturity, volatility)
            put_price = put_option_price(stock_price, strike_price, interest_rate, time_maturity, volatility)
    
            #Display The Results
            call_price_label.config(text=f"Call Option Price: ${call_price}")
            put_price_label.config(text=f"Put Option Price: ${put_price}")
    
        except ValueError:
            messagebox.showerror("Input Error", "Please input a number")


    #Calculate Button
    calculate_button = tk.Button(black_scholes, text="Calculate", command=calculate_option_prices)
    calculate_button.pack(pady=10)


