from fastapi import APIRouter
from .schemas import (
    EventSchema, 
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
    )


router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [{"id":1},{"id":2}, {"id":3}]
    }


@router.get("/{event_id}")
def get_event(event_id:int) -> EventSchema:
    return {
       "id": event_id
    }


@router.post("/")
def create_event(payload:EventCreateSchema) -> EventSchema:
    
    data = payload.model_dump()

    return {"id": 123, "page": **data} #payload.page
    

@router.put("/{event_id}")
def update_event(event_id:int, payload:EventUpdateSchema) -> EventSchema:
    data = payload.model_dump()
    return {
       "id": event_id,
       "description": **data} #payload.description
    

