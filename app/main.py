from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Serve the "static" folder
BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

@app.get("/form")
def form_page():
    return FileResponse("static/form.html")

@app.post("/api/submit")
def submit(name: str = Form(...)):
    return {"message": f"Hello, {name}!"}