import asyncio
from models import IngestRequest, IngestResponse, Batch, BatchStatus
from data_store import ingestions, add_ingestion, batch_queue
import uuid
from utils import process_batch
import time

priority_map = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}

def create_batches(ids):
    return [ids[i:i + 3] for i in range(0, len(ids), 3)]

def enqueue_batches(request: IngestRequest, ingestion_id):
    timestamp = time.time()
    batches = []

    for id_group in create_batches(request.ids):
        batch_id = str(uuid.uuid4())
        batch = Batch(batch_id=batch_id, ids=id_group, status=BatchStatus.YET_TO_START)
        batches.append(batch)
        batch_queue.append((priority_map[request.priority], timestamp, ingestion_id, batch))

    add_ingestion(ingestion_id, batches)

async def batch_worker():
    while True:
        if batch_queue:
            batch_queue.sort()
            _, _, ingestion_id, batch = batch_queue.pop(0)
            await process_batch(batch, ingestion_id)
            await asyncio.sleep(5)  # Enforce 1 batch per 5 seconds
        else:
            await asyncio.sleep(1)
