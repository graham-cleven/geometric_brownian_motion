#!/usr/bin/env python3

import numpy as np
import random
import yfinance as yf
from typing import Union, Optional
import matplotlib.pyplot as plt

def get_stock(symbol):
    symbol = yf.Ticker(symbol)                                                  
    # Reach out to Yahoo finance API to get historical data for the given stock symbol
    stock_data = symbol.history(interval="1d", period="max")   
    return stock_data


def get_gbm_for_stock_data(stock_data, period: str):
    # Calculate historical T, N, mu, sigma, and S0 values for given symbol and period
    T = (stock_data.index[-1] - stock_data.index[0]).days / 365
    N = len(stock_data)
    # 252 days per year is a generally accepted average in finance
    mu = stock_data["Close"].pct_change().mean() * 252
    # Variance is proportional to the square of time
    sigma = stock_data["Close"].pct_change().std() * np.sqrt(252)
    S0 = stock_data["Close"][0]

    # Generate geometric brownian motion matching parameters for given symbol
    return geometric_brownian_motion(T=T, N=N, mu=mu, sigma=sigma, S0=S0)


def geometric_brownian_motion(
    T: float, N: int, mu: float, sigma: float, S0: float
) -> Union[float, None]:
    # dS(t) = μS(t)dt + σS(t)dW(t)
    # T: Total time period of simulation
    # N: Time steps in simulation (252 days in a trading year)
    # mu: drift (eg. expected return of underlying asset)
    # sigma: vol.
    # S0: initial price at time 0

    print("T: ", T, "N: ", N, "mu: ", mu, "sigma: ", sigma, "S0: ", S0)

    # Calculate time step dt
    dt = T / N
    # Create time vector, t, with N equally spaced points between 0 and T
    t = np.linspace(0, T, N)
    # Generate random standard normal variable, W, of size N
    W = np.random.standard_normal(size=N)
    # Scale W by the square root of dt to get the standard brownian motion
    W = np.cumsum(W) * np.sqrt(dt)
    # Calculate the geometric brownian motion process, X
    X = (mu - 0.5 * sigma**2) * t + sigma * W
    # Calculate the asset price at each time step, S
    S = S0 * np.exp(X)
    return S


def brownian_motion(n):
    # Initialize the list with the first value
    motion = [0]
    for i in range(1, n):
        # Generate a random number between -1 and 1
        dx = random.uniform(-1, 1)
        # Add the random number to the previous value in the list
        motion.append(motion[i - 1] + dx)
    return motion


def chart_results(symbol, stock_data, samples):
    figure, axis = plt.subplots()
    plt.title(f"Geometric Brownian Motion vs. Real Close Price for {symbol}")
    stock_data.reset_index(inplace=True)
    axis.plot(stock_data["Close"], color="red")
    for result in samples:
        axis.plot(result)
    # axis.plot(stock_data['Close'])
    plt.show()


symbol = "SPY"
samples = 10
stock_data =  get_stock(symbol=symbol)
results = []
for x in range(samples):
    results.append(get_gbm_for_stock_data(stock_data=stock_data, period="1D"))
chart_results(symbol=symbol, stock_data = stock_data, samples=results)
