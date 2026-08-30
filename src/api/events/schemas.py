from pydantic import BaseModel
from typing import List, Optional

class EventSchema(BaseModel):
    id:int
    page: Optional[str] = ""


class EventCreateSchema(BaseModel):
    page: str


    
class EventUpdateSchema(BaseModel):
    description: str


class EventListSchema(BaseModel):
    results: List[EventSchema]
