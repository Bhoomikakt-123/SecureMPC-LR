SecureMPC-LR: Privacy-Preserving Linear Regression using Multi-Party Computation

This project demonstrates a privacy-preserving approach to linear regression using simulated Secure Multi-Party Computation (MPC) with PySyft. It enables multiple parties to collaboratively train a machine learning model without sharing their raw data.

🚀 Features

Simulates 3 virtual data owners (Alice, Bob, Charlie)

Trains linear regression models locally on private data

Securely aggregates model parameters

Predicts without centralizing data

Helps comply with data privacy regulations (GDPR, HIPAA, etc.)

🛠️ Tech Stack

Python

PySyft

PyTorch

Scikit-learn

Pandas

NumPy

📦 Installation

Clone the repo:

git clone https://github.com/Bhoomikakt-123/SecureMPC-LR.git

cd SecureMPC-LR

Install dependencies:

pip install -r requirements.txt

▶️ How to Run

Make sure you have Python 3.10+ installed

Run the main file:

python main.py

📌 What This Project Does:

Simulates secure collaboration between multiple parties to train a linear regression model without sharing raw data.

Uses virtual workers (Alice, Bob, Charlie) to mimic separate organizations holding private datasets.

Each party trains a local model on its private data, and model parameters are securely aggregated.

Demonstrates how machine learning can be performed in a privacy-preserving way using Multi-Party Computation (MPC).

Helps address real-world challenges where data privacy regulations prevent centralized data sharing.

💡 Project Use Cases

Privacy-Preserving Machine Learning

Secure Healthcare or Finance Model Training

Regulatory-Compliant AI Collaboration

👨‍💻 Author

BhoomikaGitHub: Bhoomikakt-123LinkedIn: linkedin.com/in/bhoomika

📜 License

This project is licensed under the MIT License.

Made with ❤️ by Bhoomika – Empowering privacy in AI.

