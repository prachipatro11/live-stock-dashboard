def train_model(data):
    data = data.dropna()   # REMOVE NaN values

    if len(data) < 5:
        raise ValueError("Not enough data to train model")

    data = data.reset_index()
    data['Days'] = np.arange(len(data))

    X = data[['Days']]
    y = data['Close']

    model = LinearRegression()
    model.fit(X, y)

    return model, data
