from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import SQLModel, Field


class EventModel(SQLModel, table=True):
    id:int
    page: Optional[str] = ""
    description: Optional[str] = ""


class EventCreateSchema(SQLModel):
    page: str


    
class EventUpdateSchema(SQLModel):
    description: str


class EventListSchema(SQLModel):
    results: List[EventSchema]
