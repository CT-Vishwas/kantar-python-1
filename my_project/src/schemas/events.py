from pydantic import BaseModel, field_validator, ValidationError, Field
from datetime import datetime

class EventRecord(BaseModel):
    event_id: str
    topic: str
    city: str
    venue_capacity: int = Field(gt=0, description="venue capacity must be greater than 0")
    scheduled_date_time: datetime

    instructor_id:str