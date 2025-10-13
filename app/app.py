from __future__ import annotations
import json
from pathlib import Path


import joblib
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError


from .schema import PredictRequest, PredictResponse
from .version import MODEL_VERSION


ARTIFACT_DIR = Path("artifacts")
MODEL_PATH = ARTIFACT_DIR / "model.pkl"


app = FastAPI(title="Virtual Diabetes Clinic – Risk Scoring API")


# Eager load model at startup
if not MODEL_PATH.exists():
raise RuntimeError("Model artifact not found. Run training first.")


MODEL = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
return {"status": "ok", "model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
try:
X = [[
req.age, req.sex, req.bmi, req.bp, req.s1, req.s2, req.s3, req.s4, req.s5, req.s6
]]
y_hat = MODEL.predict(X)[0]
return {"prediction": float(y_hat)}
except ValidationError as ve:
raise HTTPException(status_code=400, detail=json.loads(ve.json()))
except Exception as e:
raise HTTPException(status_code=400, detail=str(e))