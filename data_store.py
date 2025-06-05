from collections import defaultdict
from typing import Dict, List
from models import Batch, BatchStatus
import time

# In-memory storage
ingestions = {}
batch_queue = []

def add_ingestion(ingestion_id, batches):
    ingestions[ingestion_id] = {
        "created_time": time.time(),
        "batches": batches
    }

def get_status(ingestion_id):
    ingestion = ingestions.get(ingestion_id)
    if not ingestion:
        return None

    batch_statuses = [batch.status for batch in ingestion["batches"]]
    if all(status == BatchStatus.YET_TO_START for status in batch_statuses):
        status = "yet_to_start"
    elif all(status == BatchStatus.COMPLETED for status in batch_statuses):
        status = "completed"
    else:
        status = "triggered"

    return {
        "ingestion_id": ingestion_id,
        "status": status,
        "batches": [batch.dict() for batch in ingestion["batches"]],
        "created_time": ingestion["created_time"]
    }
