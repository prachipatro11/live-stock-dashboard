import yfinance as yf

def get_stock_data(ticker):
    data = yf.download(ticker, period="1mo", interval="1d")

    # HANDLE EMPTY DATA
    if data.empty:
        return None

    return data
