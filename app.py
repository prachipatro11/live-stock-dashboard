import streamlit as st
from data_fetch import get_stock_data
from model import train_model, predict_next

# ------------------- UI HEADER -------------------
st.title("📊 Real-Time Stock Analytics Dashboard")
st.caption("Live data + basic ML prediction")

# ------------------- STOCK INPUT -------------------
ticker = st.selectbox("Select Stock", ["AAPL", "TSLA", "GOOG", "MSFT"])

# ------------------- FETCH DATA -------------------
data = get_stock_data(ticker)

# ------------------- ERROR HANDLING -------------------
if data is None or data.empty:
    st.error("Invalid stock symbol or no data found.")

else:
    # ------------------- DATA CLEANING -------------------
    data = data.reset_index()
    data = data.set_index('Date')

    # ------------------- SHOW DATA -------------------
    st.subheader("📄 Recent Data")
    st.write(data.tail())

    # ------------------- METRIC -------------------
    latest_price = data['Close'].iloc[-1]
    st.metric("Latest Price", round(latest_price, 2))

    # ------------------- CHART -------------------
    st.subheader("📈 Stock Price Chart")
    st.line_chart(data[['Close']])

    # ------------------- ML MODEL -------------------
    model, df = train_model(data)
    prediction = predict_next(model, df)

    # ------------------- PREDICTION -------------------
    st.subheader("🔮 Prediction")
    st.success(f"Predicted Next Price: {round(prediction, 2)}")