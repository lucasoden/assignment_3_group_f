# Diabetes risk prediction


Predicts short‑term diabetes progression as JSON files.

**Note:** Docker Desktop required to be installed and running before attempting.

---

## Pull from github repo
```bash
docker pull ghcr.io/lucasoden/assignment_3_group_f:v0.1
```
## Run container locally
```bash
docker run -p 8000:8000 ghcr.io/lucasoden/assignment_3_group_f:v0.1
```
## Check health through GET
```bash
curl http://localhost:8000/health
```
## Check prediction (with example variables) through POST
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"age\":0.02,\"sex\":-0.044,\"bmi\":0.06,\"bp\":-0.03,\"s1\":-0.02,\"s2\":0.03,\"s3\":-0.02,\"s4\":0.02,\"s5\":0.02,\"s6\":-0.001}"
```

