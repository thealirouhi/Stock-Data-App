import yfinance as yf
import streamlit as st
import datetime

tickerSymbol = "GOOGL"
st.write("""
    # Market Data – Price & Volume
         

"""
)

tickerSymbol = st.selectbox(
    "Ticker Symbol",
    ("GOOGL", "AAPL", "ADBE","ABNB","AMZN"),
    index=0,
    placeholder="Select ticker symbol...",
)

startDate = st.date_input("Start date", datetime.date(2010, 1, 1))

endDate = st.date_input("End date", datetime.date(2020, 1, 1),max_value="today")

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period="1d", start=startDate,end=endDate)
st.write("""tickerSymbol""",tickerSymbol
    )
st.write("""
    ## Closing price
"""
)
st.line_chart(tickerDF.Close)

st.write("""
    ## Volume
"""
)

st.line_chart(tickerDF.Volume)