import sys
from pathlib import Path

# Allow importing src/
sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.models.inference import load_model
from src.models.inference import predict_text

import logging
from datetime import datetime
import os

# Logging setup
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# ------------------------------
# FASTAPI INIT
# ------------------------------

app = FastAPI(
    title="ATC-SAFE API",
    description="ATC NLP Classification Backend",
    version="1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# LOAD MODEL
# ------------------------------

print("🔄 Loading Transformer model...")
model, tokenizer, id2label = load_model()
print("✅ Model Loaded Successfully!")

# ------------------------------
# REQUEST MODEL
# ------------------------------

class InputText(BaseModel):
    text: str

# ------------------------------
# ENDPOINTS
# ------------------------------

@app.get("/")
def root():
    return {"message": "ATC NLP API running ✅"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_route(data: InputText):
    result = predict_text(data.text, model, tokenizer, id2label)

    # ✅ ADDED — Log every prediction
    logging.info(
        f'Text="{data.text[:40]}..." → Prediction="{result["label"]}" — Conf={result["confidence"]:.4f}'
    )

    return {
        "prediction": result["label"],
        "confidence": result["confidence"]
    }

# ------------------------------
# MAIN (for python api/main.py)
# ------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
