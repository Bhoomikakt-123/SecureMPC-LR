import numpy as np

def average_models(coefs, intercepts):
    avg_coef = sum(coefs) / len(coefs)
    avg_intercept = sum(intercepts) / len(intercepts)
    return avg_coef, avg_intercept
