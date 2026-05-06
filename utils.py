import matplotlib.pyplot as plt

def plot_data(data):
    plt.figure(figsize=(10,5))
    plt.plot(data['Close'])
    plt.title("Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()