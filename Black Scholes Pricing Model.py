import math
import numpy #install
import scipy #install
import matplotlib #install

# Inputs:
stock_price = input("Current stock price: ")
strike_price = input("Strike price: ")
interest_rate = input("Risk-free interest rate: ")
time_maturity = input("Time to maturity: ")
volatility = input("Volatility(%): ") / 100

normal_dist = scipy.stats.norm.cdf

# Black-Scholes Formulas:
d1 = (math.log(stock_price/strike_price) + (interest_rate + ))

d2 = d1 - (volatility * (time_maturity^0.5))

#Call Option:
call_option_price = (stock_price * normal_dist * d1) - (strike_price * (math.e^( -1 * interest_rate * time_maturity)) * normal_dist * d2)

#Put Option:
put_option_price = (strike_price * (math.e^( -1 * interest_rate * time_maturity)) * normal_dist * (-1 * d2)) - (stock_price * normal_dist * (-1 * d1))

