import yfinance as yf
import pandas as pd

data = yf.Ticker("SPY")
df = data.history(period="5y")

df[['Open', 'High', 'Low', 'Close']].to_csv("spydata.csv")
print("Data saved successfully!")
