import math
from scipy.stats import norm

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
