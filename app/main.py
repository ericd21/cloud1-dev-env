from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your first Codespaces Python app!"}

@app.get("/status")
def status():
    return {"status": "running", "environment": "codespaces"}
