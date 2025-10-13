# Virtual Diabetes Clinic – Risk Scoring API


Predicts short‑term diabetes progression (demo) and serves a numeric risk score.


## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m ml.train
uvicorn app.app:app --host 0.0.0.0 --port 8000