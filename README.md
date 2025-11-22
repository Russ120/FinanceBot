# Telegram Bot en Vercel (Python + FastAPI)

## Pasos
1. Sube estos archivos a un repo y conéctalo a Vercel.
2. En Vercel: Settings → Environment Variables
   - TELEGRAM_BOT_TOKEN = <tu token de BotFather>
3. Despliega.
4. Configura el webhook:
   curl -F "url=https://TU-PROYECTO.vercel.app/api/telegram" https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook

## Uso
- /start, /help, /ping
- texto libre → echo
