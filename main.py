from fastapi import FastAPI
import models
from routes import router
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/book", tags=["book"])

@app.get("/")
async def root():
    return {'message':"/docs FastAPI Swagger bolimiga o'ting"}

@app.post('/login')
async def login():
    return "ThisTokenIsFake"

