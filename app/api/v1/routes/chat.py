from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.rag_chain import get_rag_chain

router = APIRouter()
qa_chain = get_rag_chain()

@router.post("/chat", response_model=ChatResponse)
def chat_with_rag(payload: ChatRequest):
    response = qa_chain.run(payload.query)
    return ChatResponse(result=response)