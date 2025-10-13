# Build stage
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ml/ ml/
COPY app/ app/
# Train at build time so the image is self-contained
RUN python -m ml.train


# Runtime stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=build /app /app
EXPOSE 8000
HEALTHCHECK CMD python -c "import requests; import sys;\n\nimport os;\nimport json;\nfrom urllib.request import urlopen\n\ntry:\n resp = urlopen('http://localhost:8000/health', timeout=2)\n sys.exit(0 if resp.getcode()==200 else 1)\nexcept Exception:\n sys.exit(1)" || exit 1
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]