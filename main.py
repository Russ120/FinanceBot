# bot.py - Bot mínimo con python-telegram-bot v20
# ⚠️ No subas tu TOKEN a internet/Repos públicos
# bot_regex.py
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import re
import os
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# TOKEN = "8551527838:AAGTdlY2XsGPs2Pye2XwDQvZZffdnIwQo3o"

# /help
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos:\n/start - saludo\n/help - ayuda\n/precio - precio de hoy")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Escríbeme: hola | precio | adios")

async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Holaaa! ¿Qué tal? 😎")

async def precio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("El precio de hoy es RD$499. (demo)")

async def adios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Nos vemos! 👋")

async def desconocido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("No te entendí. Prueba: hola, precio o adios.")





def main():
    app = Application.builder().token(TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("help", help_cmd))


    pp = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("precio", precio))


    # Coincidencias por texto/regex (ignora mayúsculas)
    app.add_handler(MessageHandler(filters.Regex(re.compile(r"^hola$", re.IGNORECASE)), hola))
    app.add_handler(MessageHandler(filters.Regex(re.compile(r"^precio$", re.IGNORECASE)), precio))
    app.add_handler(MessageHandler(filters.Regex(re.compile(r"^adios?$", re.IGNORECASE)), adios))

    # Cualquier otra cosa
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, desconocido))


    print("Bot corriendo... Ctrl+C para parar")
    app.run_polling()

if __name__ == "__main__":
    main()
