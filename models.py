from enum import Enum
from pydantic import BaseModel
from typing import List
import uuid

class Priority(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class IngestRequest(BaseModel):
    ids: List[int]
    priority: Priority

class IngestResponse(BaseModel):
    ingestion_id: str

class BatchStatus(str, Enum):
    YET_TO_START = "yet_to_start"
    TRIGGERED = "triggered"
    COMPLETED = "completed"

class Batch(BaseModel):
    batch_id: str
    ids: List[int]
    status: BatchStatus
