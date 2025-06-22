from fastapi import FastAPI
from app.api.v1.routes.chat import router as chat_router

app = FastAPI(title=" Chatbot Routes")

app.include_router(chat_router, prefix="/api/v1", tags=["Chatbot"])
