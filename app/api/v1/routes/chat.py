from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.schemas import ChatRequest, ChatResponse, ChatCreate, ChatRead
from app.services.rag_chain import get_rag_chain
from app.core.security import get_current_user
from app.db.session import get_session
from app.db.models import Chat, User

router = APIRouter()
qa_chain = get_rag_chain()

@router.post("/chat", response_model=ChatResponse)
def chat_with_rag(payload: ChatRequest, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    response = qa_chain.run(payload.query)
    chat = Chat(user_id=current_user.id, query=payload.query, response=response)
    session.add(chat)
    session.commit()
    session.refresh(chat)
    return ChatResponse(result=response)

@router.get("/chat", response_model=list[ChatRead])
def get_user_chats(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    chats = session.exec(select(Chat).where(Chat.user_id == current_user.id)).all()
    return chats