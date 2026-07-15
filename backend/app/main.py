from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.chat import ask_gemini

app = FastAPI(title="Chota AI")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Welcome to Chota AI 🚀"}


@app.post("/chat")
def chat(req: ChatRequest):
    reply = ask_gemini(req.message)
    return {"reply": reply}