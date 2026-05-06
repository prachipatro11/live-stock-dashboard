data = get_stock_data(ticker)

if data is None or data.empty:
    st.error("Invalid stock symbol or no data found.")
else:
    st.subheader("Stock Data")
    st.write(data.tail())

    st.line_chart(data['Close'])

    model, df = train_model(data)
    prediction = predict_next(model, df)

    st.subheader("Predicted Next Price")
    st.write(prediction)
