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

To run fastapi application:::: poetry run uvicorn main:app --reload

To build a docker:: docker build -t my-python-app .
To run the docker:: docker run --rm -p 8000:8000 my-python-app
To validate: http://localhost:8000
"""