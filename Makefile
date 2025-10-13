.PHONY: venv install train run test docker
venv:
python -m venv .venv
. .venv/bin/activate && pip install -U pip
install:
. .venv/bin/activate && pip install -r requirements.txt
train:
. .venv/bin/activate && python -m ml.train
run:
. .venv/bin/activate && uvicorn app.app:app --host 0.0.0.0 --port 8000
test:
. .venv/bin/activate && pytest -q


docker:
docker build -t ghcr.io/ORG/REPO:v0.1 .