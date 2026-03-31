import yfinance as yf
def get_stock_price(ticker):
    try:
        data = yf.download(ticker, period="1d")
        return float(data['Close'].iloc[-1])
    except:
        return None
