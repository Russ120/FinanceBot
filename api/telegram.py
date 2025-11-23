from fastapi import Request
from telegram import Update
from bot import app_tg

async def handler(request: Request):
    data = await request.json()
    update = Update.de_json(data, app_tg.bot)
    await app_tg.process_update(update)
    return {"ok": True}
