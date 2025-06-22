from fastapi import FastAPI
from app.api.v1.routes.chat import router as chat_router
from app.api.v1.routes.auth import router as auth_router  
from app.db.models import SQLModel
from app.db.session import engine

app = FastAPI(title="🤖 Chatbot + Auth API")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(chat_router, prefix="/api/v1", tags=["Chatbot"])
app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": " API is running! Visit http://localhost:8080/docs"}
