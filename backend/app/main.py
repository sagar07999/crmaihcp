from fastapi import FastAPI
from app.routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes.interaction import router as interaction_router

app = FastAPI(title="AI CRM HCP Module")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chat_router)
Base.metadata.create_all(bind=engine)

app.include_router(interaction_router)


@app.get("/")
def home():
    return {"message": "AI CRM Backend Running"}