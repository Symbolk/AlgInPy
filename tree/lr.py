import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.w = w
        self.b = b
        self.learning_rate = learning_rate
        self.iterations = iterations

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        self.b = 0

        for _ in range(self.iterations):
            y_pred = self.predict(X)

            loss = np.mean((y_pred - y) ** 2)

            dw =