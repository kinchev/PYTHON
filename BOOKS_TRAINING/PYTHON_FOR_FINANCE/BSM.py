import numpy as np


import numpy as np
from scipy.stats import norm

interest_rate_r=0.01
underlying_price_S=30
strike_price_K=40
time_T=240/365
volatility_sigma=0.30

def black_scholes(interest_rate_r,underlying_price_S,strike_price_K,time_T,volatility_sigma,type="C"):
    "Calculate BSM option price for call/put"
    natural_log_d1=(np.log(underlying_price_S/strike_price_K)+(interest_rate_r+volatility_sigma**2/2)*time_T)/(volatility_sigma*np.sqrt(time_T))
    d2=natural_log_d1-volatility_sigma*np.sqrt(time_T)
    try:
            if type=="C":
                price=underlying_price_S*norm.cdf(natural_log_d1,0,1)-strike_price_K*np.exp(-interest_rate_r*time_T)*norm.cdf(d2,0,1)
            elif type=="P":
                price=strike_price_K*np.ecp(interest_rate_r*time_T)*norm.cdf(-d2,0,1)-underlying_price_S*norm.cdf(natural_log_d1,0,1)
            return price
    except:
            print("Please confirm all option parameters above!!!")
            
print("Option Price is: ",round(black_scholes(interest_rate_r,underlying_price_S,strike_price_K,time_T,volatility_sigma,type="C"),2))                
            
            
            
        
