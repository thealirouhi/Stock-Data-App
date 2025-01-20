import yfinance as yf
import streamlit as st

st.write("""
    # hello world!
"""
)

tickerSymbol = st.text_input("Ticker Symbol", "GOOGL")

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period="1d", start='2010-01-01',end='2020-01-01')