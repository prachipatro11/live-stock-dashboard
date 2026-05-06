import yfinance as yf

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")

        if data is None or data.empty:
            return None

        return data

    except Exception:
        return None
