# main.py
import os
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from telegram import Update
from bot import app_tg

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await app_tg.initialize()
    await app_tg.start()
    print("Bot inicializado en Vercel 🚀")
    yield
    await app_tg.stop()
    await app_tg.shutdown()

app = FastAPI(lifespan=lifespan)

@app.post("/api/telegram")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, app_tg.bot)
    await app_tg.process_update(update)
    return {"ok": True}

@app.get("/")
async def home():
    return {"message": "Telegram Bot activo en Vercel 🟢"}
