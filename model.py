from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(data):
    data = data.reset_index()
    data['Days'] = np.arange(len(data))

    X = data[['Days']]
    y = data['Close']

    model = LinearRegression()
    model.fit(X, y)

    return model, data

def predict_next(model, data):
    next_day = [[len(data)]]
    prediction = model.predict(next_day)
    return prediction[0]