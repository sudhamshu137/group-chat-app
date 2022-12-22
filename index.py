from fastapi import FastAPI
from routes.message import mes

app = FastAPI()
app.include_router(mes)