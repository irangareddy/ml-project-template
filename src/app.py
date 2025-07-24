from fastapi import FastAPI
from src.hello import say_hello

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": say_hello()}


@app.get("/health")
def health_check():
    return {"status": "ok"}
