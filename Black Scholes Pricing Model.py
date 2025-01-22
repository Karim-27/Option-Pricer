import math
import numpy
import matplotlib 
from scipy.stats import norm
import tkinter

# Inputs:
stock_price = float(input("Current stock price: "))
strike_price = float(input("Strike price: "))
interest_rate = float(input("Risk-free interest rate(%): ")) / 100
time_maturity = float(input("Time to maturity(years): "))
volatility = float(input("Volatility(%): ")) / 100

#Checking Invalid Inputs:

if stock_price < 0:
    raise ValueError("Stock price must be greater than 0")
elif strike_price < 0:
    raise ValueError("Strike price must be greater than 0")
elif time_maturity < 0:
    raise ValueError("Time to maturity must be greater than 0")
elif volatility < 0:
    raise ValueError("Volatility must be greater than 0")


# Black-Scholes Formulas:
d1 = (math.log(stock_price/strike_price) + ((interest_rate + \
    ((volatility**2)/2)) * time_maturity)) / (volatility * (time_maturity**0.5))       

d2 = d1 - (volatility * (time_maturity**0.5))

c_norm_cdf_d1 = norm.cdf(d1)
c_norm_cdf_d2 = norm.cdf(d2)
p_norm_cdf_d1 = norm.cdf(-1 * d1)
p_norm_cdf_d2 = norm.cdf(-1 * d2)


#Call Option:
def call_option_price(stock_price, strike_price, interest_rate, time_maturity,\
                      volatility, c_norm_cdf_d1, c_norm_cdf_d2):
    
    call_price = (stock_price * c_norm_cdf_d1) - (strike_price * (math.e**( -1\
                    * interest_rate * time_maturity)) * c_norm_cdf_d2)
    
    return call_price

#Put Option:
def put_option_price(stock_price, strike_price, interest_rate, time_maturity, \
                     volatility, p_norm_cdf_d1, p_norm_cdf_d2):
    
    put_price = (strike_price * (math.e**(-1 * interest_rate * time_maturity))\
                 * p_norm_cdf_d2) - (stock_price * p_norm_cdf_d1)
    
    return put_price



