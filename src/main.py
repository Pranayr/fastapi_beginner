from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



"""
# FastAPI = web framework
# Uvicorn = web server

                    WEB SERVER
                  ┌─────────────┐
Browser ────────► │   Uvicorn   │
                  └──────┬──────┘
                         │
                         │ ASGI
                         ▼
                  ┌─────────────┐
                  │   FastAPI   │
                  │     app     │
                  └──────┬──────┘
                         │
                         ▼
                  Your Python code

Yes , you can remove uvicorn but, you still need an ASGI server (or another compatible server).
Uvicorn is just one ASGI server.
For example, you could use:
Uvicorn — most common for FastAPI development
Hypercorn
"""