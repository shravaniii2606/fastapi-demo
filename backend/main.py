from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend running from VS Code"}

@app.get("/hello")
def hello(name: str):
    print(f"Received text: {name}")
    return {"reply": f"Hello {name}, backend connected 🎉"}
