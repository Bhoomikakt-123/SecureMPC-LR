import torch
import numpy as np
from src.workers import create_workers
from src.data_loader import load_and_split_data
from src.local_model import train_local_model
from src.aggregation import average_models
from src.predict import predict

# Step 1: Setup workers
alice, bob, charlie = create_workers()

# Step 2: Load and split data
X_parts, y_parts = load_and_split_data("data/dataset.csv")

# Step 3: Send to virtual workers
X1, y1 = torch.tensor(X_parts[0], dtype=torch.float32).send(alice), torch.tensor(y_parts[0], dtype=torch.float32).send(alice)
X2, y2 = torch.tensor(X_parts[1], dtype=torch.float32).send(bob), torch.tensor(y_parts[1], dtype=torch.float32).send(bob)
X3, y3 = torch.tensor(X_parts[2], dtype=torch.float32).send(charlie), torch.tensor(y_parts[2], dtype=torch.float32).send(charlie)

# Step 4: Train local models
coef1, int1 = train_local_model(X1, y1)
coef2, int2 = train_local_model(X2, y2)
coef3, int3 = train_local_model(X3, y3)

# Step 5: Aggregate models
avg_coef, avg_intercept = average_models([coef1, coef2, coef3], [int1, int2, int3])

print("Average Coefficients:", avg_coef)
print("Average Intercept:", avg_intercept)

# Step 6: Predict
x_test = np.array([[7.0, 8.0]])
y_pred = predict(x_test, avg_coef, avg_intercept)
print("Prediction for input [7.0, 8.0]:", y_pred)
