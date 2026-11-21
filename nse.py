import yfinance as yf

# 1. NSE stock select karein (Stock name ke aage .NS lagana zaroori hai)
data = yf.download("HDFCBANK.NS", period="1y", interval="1d")

# 2. Data ko computer mein Excel/CSV file banakar save karein
data.to_csv("nse_data.csv")
