# ✈️ ATC-SAFE: NLP-Based ATC Communication Analysis

ATC-SAFE is an NLP-based system designed to analyze Air Traffic Control (ATC) incident narratives and categorize them into operational risk domains.  
The goal is to assist aviation safety stakeholders in identifying potential hazards arising from miscommunication, operational deviations, or technical anomalies.

---

## ✅ Why This Project?

2025 saw multiple aviation incidents where investigations pointed to **miscommunication between pilots and ATC** as a recurring factor.  
Manually reviewing narrative safety reports (e.g., ASRS) is time-consuming and inefficient at scale.

ATC-SAFE introduces:  
✅ Automated narrative interpretation  
✅ Risk-category classification  
✅ Confidence-based decision support  

This helps safety teams prioritize hazards, identify patterns, and respond faster.

---

## ✅ Features

- Deep Learning–based text classification (DistilBERT)
- FAA ASRS dataset preprocessing (~4.5K structured reports)
- Modular & scalable ML pipeline
- Prediction + confidence scoring
- FastAPI backend
- Minimal UI (HTML/CSS)
- Logging + health endpoints
- Docker-based packaging (ready for cloud)

---

## ✅ Tech Stack

| Layer     | Tools       |
|-----------|-------------|
| Language  | Python      |
| NLP Model | DistilBERT  |
| Framework | FastAPI     |
| UI        | HTML + CSS  |
| MLOps     | Docker      |
| Logging   | Python logging |
| Data      | FAA ASRS narratives |

---

## ✅ Project Structure

ATC-Safe-NLP/
│
├── api/ # FastAPI backend
├── src/
│ ├── data/ # data handling
│ ├── models/ # training + inference
│ └── utils/ # helpers
├── models/ # saved distilbert model
├── ui/ # frontend
├── logs/ # prediction logs
├── requirements.txt
├── Dockerfile
└── README.md


---

## ✅ How It Works

1️⃣ User submits narrative text  
2️⃣ Transformer model processes text  
3️⃣ Model predicts risk category + confidence  
4️⃣ Output shown via API/UI  
5️⃣ Prediction logged for analysis  

---

## ✅ Run Locally

### 1) Create environment
```bash
conda create -n atccom python=3.10
conda activate atccom
pip install -r requirements.txt
uvicorn api.main:app --reload
View docs:
http://127.0.0.1:8000/docs
cd ui
python -m http.server 5500
```

✅ Docker Support
Build
docker build -t atc-safe .

Run
docker run -p 8000:8000 atc-safe

✅ Future Enhancements

AWS EC2 deployment

Speech-to-text integration (Live ATC)

Incident similarity search

Severity scoring

Dashboard analytics

✅ Dataset

FAA ASRS incident narratives (public safety reporting system)
Processed & structured for training.

✅ Author

👤 Ayush Mishra
🔗 GitHub: https://github.com/ayush-mishra7

✅ License

MIT
