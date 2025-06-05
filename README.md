# Data Ingestion API System

## 🚀 Features

- Ingests data in priority order.
- Processes 3 IDs per batch asynchronously.
- Respects 5-second rate limit per batch.
- Status API to check batch and ingestion status.

## 🔧 Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
