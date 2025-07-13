from sklearn.linear_model import LinearRegression

def train_local_model(X, y):
    X_np = X.get().numpy()
    y_np = y.get().numpy()
    model = LinearRegression()
    model.fit(X_np, y_np)
    return model.coef_, model.intercept_
