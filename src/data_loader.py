import pandas as pd
import numpy as np

def load_and_split_data(file_path):
    data = pd.read_csv(file_path)
    X = data[['X1', 'X2']].values
    y = data['Y'].values
    return np.array_split(X, 3), np.array_split(y, 3)
