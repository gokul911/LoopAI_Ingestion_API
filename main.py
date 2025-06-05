from fastapi import FastAPI, HTTPException
from ingestion_service import enqueue_batches, batch_worker
from data_store import get_status
from models import IngestRequest, IngestResponse
import uuid
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(batch_worker())

@app.post("/ingest", response_model=IngestResponse)
async def ingest(request: IngestRequest):
    ingestion_id = str(uuid.uuid4())
    enqueue_batches(request, ingestion_id)
    return {"ingestion_id": ingestion_id}

@app.get("/status/{ingestion_id}")
async def status(ingestion_id: str):
    status = get_status(ingestion_id)
    if not status:
        raise HTTPException(status_code=404, detail="Ingestion ID not found")
    return status
