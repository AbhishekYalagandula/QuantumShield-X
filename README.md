# 🛡️ QuantumShield-X

> **AI Powered Post-Quantum Cryptography Readiness & Vulnerability Scanner**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Qiskit](https://img.shields.io/badge/Qiskit-Quantum-purple?logo=qiskit)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 🌍 Overview

QuantumShield-X is an **AI-powered Quantum Cybersecurity Platform** that helps organizations prepare for the **Post-Quantum Computing Era**.

As quantum computers evolve, traditional cryptographic algorithms like **RSA**, **ECC**, and **SHA-1** become vulnerable to attacks such as **Harvest Now, Decrypt Later (HNDL)**.

QuantumShield-X automatically scans software projects, identifies vulnerable cryptographic implementations, predicts quantum risks using **Quantum Machine Learning**, generates AI recommendations, and provides migration strategies toward **NIST-approved Post-Quantum Cryptography (PQC)** algorithms.

---

# 🚀 Features

## 📂 Smart Project Upload

- Upload ZIP source code
- Automatic extraction
- Multi-language project support

---

## 🔍 Cryptographic Scanner

Automatically detects:

- 🔐 RSA
- 🔐 ECC
- 🔐 SHA-1
- 🔐 TLS
- 🔐 AES
- 🔐 SHA-256
- 🔐 DES

---

## 🤖 Quantum Machine Learning

Uses **Qiskit Machine Learning** to:

- Predict project quantum risk
- Classify vulnerability level
- Generate confidence score

---

## 🧠 Explainable Quantum AI (XQAI)

Provides:

- Feature Importance
- Confidence Score
- AI Explanations
- Decision Transparency

---

## ⚠️ Quantum Risk Engine

Calculates:

- Quantum Risk Score
- Risk Level
- Vulnerable Algorithms
- Safe Algorithms
- Migration Progress

---

## 📊 Interactive Dashboard

Displays:

- 📈 Risk Gauge
- 📉 Risk Trend
- 🧩 Quantum Readiness
- 📝 Recent Scans
- ⚡ Quick Actions

---

## 🔄 Migration Planner

Automatically recommends migration:

| Vulnerable | Replace With |
|------------|--------------|
| RSA | ML-KEM (CRYSTALS-Kyber) |
| ECC | ML-DSA (Dilithium) |
| SHA-1 | SHA-3 |
| TLS | PQC Enabled TLS |

---

## 💻 Secure Code Generator

Generate secure implementation for:

- ML-KEM
- ML-DSA
- AES-256
- SHA-3

---

## 📑 Automated Report Generation

Generates:

- PDF Security Report
- Migration Report
- Risk Summary

---

## 📈 Benchmark Engine

Compares your project with:

- Enterprise Standards
- Industry Average
- Quantum Readiness

---

## 🛡️ Audit Logging

Tracks:

- Upload History
- User Activity
- Report Downloads
- Security Events

---

# 🏗️ System Architecture

```
ZIP Upload
      │
      ▼
Project Extraction
      │
      ▼
Code Scanner
      │
      ▼
Algorithm Detection
      │
      ▼
Quantum Risk Engine
      │
      ▼
Quantum ML Predictor
      │
      ▼
Explainable AI
      │
      ▼
Migration Planner
      │
      ▼
Dashboard
      │
      ▼
PDF Report
```

---

# 🧠 Technology Stack

## Frontend

- ⚛️ React.js
- HTML5
- CSS3
- JavaScript
- React Icons

---

## Backend

- ⚡ FastAPI
- Python
- SQLAlchemy
- SQLite

---

## Quantum Computing

- Qiskit
- Qiskit Machine Learning
- Variational Quantum Classifier (VQC)

---

## AI

- Quantum Machine Learning
- Explainable AI (XQAI)

---

## Database

- SQLite

---

# 📂 Project Structure

```
QuantumShield-X
│
├── frontend
│   ├── components
│   ├── pages
│   ├── layouts
│   └── assets
│
├── backend
│   ├── app
│   │
│   ├── routes
│   ├── services
│   ├── scanner
│   ├── qml
│   ├── quantum
│   ├── database
│   ├── benchmark
│   ├── xqai
│   ├── report
│   └── auth
│
├── uploads
├── reports
├── extracted_projects
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/QuantumShield-X.git
```

```
cd QuantumShield-X
```

---

## Backend

```
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```
cd frontend

npm install

npm run dev
```

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| POST /upload | Upload Project |
| GET /dashboard | Dashboard |
| GET /risk | Quantum Risk |
| GET /migration | Migration Plan |
| GET /report/latest | Download Report |
| POST /migration/generate | Generate Secure Code |

---

# 🎯 Supported Algorithms

### Vulnerable

- RSA
- ECC
- SHA-1
- TLS
- DES

### Secure

- AES-256
- SHA-256
- SHA-3
- ML-KEM
- ML-DSA

---

# 🖥️ Screenshots

- 🏠 **Dashboard**
  
  <img width="1913" height="902" alt="image" src="https://github.com/user-attachments/assets/0075cc2b-5183-42db-a3a3-8d4be0030e74" />

  <img width="1883" height="864" alt="image" src="https://github.com/user-attachments/assets/8afceb39-e29d-404e-98a4-6ec7164970d6" />

  <img width="1868" height="883" alt="image" src="https://github.com/user-attachments/assets/d244460f-95a1-4420-bc08-4d86c8554eec" />



- 📤 **Upload Page**
  
  <img width="1911" height="894" alt="image" src="https://github.com/user-attachments/assets/f3e81e85-84ca-4294-8522-fd1a382b2f8c" />

  

- 🔍 **Scanner**
  
  <img width="1919" height="902" alt="image" src="https://github.com/user-attachments/assets/8195bd2e-2144-46eb-80a3-4f421ab4824e" />


- 📊 **Risk Analysis**
  
  <img width="1917" height="911" alt="image" src="https://github.com/user-attachments/assets/aea87547-1c62-42bb-a039-5631732392c8" />

- 🧠 **Explainable AI**
  
  <img width="1915" height="897" alt="image" src="https://github.com/user-attachments/assets/e7e529d9-a12d-452e-b9a3-ce30db68f61e" />

  
- 🔄 **Migration Planner**
  
  <img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/400e91e2-834a-4d53-a9ec-d4639898dd49" />

- 📄 **PDF Report**
  
  <img width="1915" height="912" alt="image" src="https://github.com/user-attachments/assets/39cbf8ba-6b36-4935-96c0-717b10af8d86" />


---

# 📈 Future Scope

- ☁️ Cloud Deployment
- 🔒 Live GitHub Repository Scanning
- 📦 Docker Support
- ☸️ Kubernetes Support
- 🤖 LLM Security Assistant
- 🔔 Real-time Threat Alerts
- 🛰️ Enterprise Multi-user Support
- 📜 Compliance Checker
- 🌍 Zero Trust Quantum Security

---

# 👨‍💻 Team

### QuantumShield-X Development Team

- 👨‍💻 Abhishek Yalagandula
- 👨‍💻 Dhammu Dilip Kumar
- 👨‍💻 Teja Vemavarapu
- 👨‍💻 Mahesh Injarapu

🏫 NRI Institute Of Technology

---

# 🏆 Achievements

✅ Quantum Machine Learning

✅ Explainable AI

✅ Automated Cryptographic Scanner

✅ Migration Planner

✅ Secure Code Generator

✅ Quantum Readiness Assessment

✅ Interactive Dashboard

✅ PDF Report Generation

---

# 📜 License

MIT License

---

# ⭐ Support

If you like this project,

⭐ Star this repository

🍴 Fork it

📢 Share it

---

# 🚀 QuantumShield-X

> **Securing Today's Software for Tomorrow's Quantum World 🌍⚛️**
