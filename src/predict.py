import numpy as np

def predict(x_input, coef, intercept):
    return np.dot(x_input, coef) + intercept
