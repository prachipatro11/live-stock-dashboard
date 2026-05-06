import streamlit as st
from data_fetch import get_stock_data
from model import train_model, predict_next

st.title("📈 Live Stock Dashboard")

ticker = st.text_input("Enter Stock Symbol", "AAPL")

data = get_stock_data(ticker)

st.subheader("Stock Data")
st.write(data.tail())

st.line_chart(data['Close'])

model, df = train_model(data)
prediction = predict_next(model, df)

st.subheader("Predicted Next Price")
st.write(prediction)