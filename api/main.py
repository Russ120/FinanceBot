from fastapi import FastAPI, Request
from telegram import Update
from bot import app_tg

app = FastAPI()

@app.post("/api/telegram")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, app_tg.bot)

    # 🚀 IMPORTANTE: Inicializar bot en serverless
    if not app_tg.running:
        await app_tg.initialize()
        await app_tg.start()

    await app_tg.process_update(update)
    return {"ok": True}
