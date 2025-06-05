import asyncio
import uuid
from models import Batch, BatchStatus
from data_store import ingestions

async def fetch_data(id):
    await asyncio.sleep(1)
    return {"id": id, "data": "processed"}

async def process_batch(batch: Batch, ingestion_id: str):
    batch.status = BatchStatus.TRIGGERED
    for id in batch.ids:
        await fetch_data(id)
    batch.status = BatchStatus.COMPLETED
