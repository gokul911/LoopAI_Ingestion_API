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
```

⚠️ Important: This project is hosted on Render's free tier. Due to platform limitations, the API instance automatically spins down after periods of inactivity. As a result, the first request after a period of no usage may take up to 50 seconds or more to receive a response. Subsequent requests will respond normally.