# SecureMPC-LR: Privacy-Preserving Linear Regression using Multi-Party Computation

This project demonstrates a privacy-preserving approach to linear regression using simulated Secure Multi-Party Computation (MPC) with PySyft. It enables multiple parties to collaboratively train a machine learning model without sharing their raw data.

## 🚀 Features
- Simulates 3 virtual data owners (Alice, Bob, Charlie)
- Trains linear regression models locally on private data
- Securely aggregates model parameters
- Predicts without centralizing data
- Helps comply with data privacy regulations (GDPR, HIPAA, etc.)

## 🛠️ Tech Stack
- Python  
- PySyft  
- PyTorch  
- Scikit-learn  
- Pandas  
- NumPy

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Bhoomikakt-123/SecureMPC-LR.git
cd SecureMPC-LR

**Install dependencies:**
```bash
pip install -r requirements.txt
```

## ▶️ How to Run

**Ensure Python 3.10+ is installed**

**Execute the main script:**
```bash
python main.py
```

## 📌 What This Project Does

- Enables multiple parties to jointly train a linear regression model without revealing their individual datasets.
- Simulates virtual data holders (Alice, Bob, Charlie) using PySyft Virtual Machines.
- Trains separate models on each dataset and securely aggregates their coefficients.
- Supports secure prediction on new inputs using aggregated model parameters.
- Solves the problem of privacy in collaborative machine learning environments.

## 💡 Use Cases

- Privacy-Preserving Machine Learning  
- Secure Healthcare Data Modeling  
- Financial Institutions Data Sharing  
- Cross-organization AI Collaboration under Data Privacy Laws

## 👨‍💻 Author

**Bhoomika**  
GitHub: [Bhoomikakt-123](https://github.com/Bhoomikakt-123)  
LinkedIn: [https://linkedin.com/in/bhoomika](https://linkedin.com/in/bhoomika)


Made with ❤️ by Bhoomika – Empowering privacy in AI.

