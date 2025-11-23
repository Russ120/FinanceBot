# bot.py
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import re
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app_tg = Application.builder().token(TOKEN).build()

# ===== HANDLERS =====
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos:\n/start\n/help\n/precio")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Escríbeme: hola | precio | adios")

async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Holaaa! 😎")

async def precio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("El precio de hoy es RD$499 (demo)")

async def adios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Nos vemos bro! 👋")

async def desconocido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("No te entendí. Prueba: hola, precio o adios.")

# ===== REGEX =====
app_tg.add_handler(CommandHandler("help", help_cmd))
app_tg.add_handler(CommandHandler("start", start))
app_tg.add_handler(CommandHandler("precio", precio))

app_tg.add_handler(MessageHandler(filters.Regex(re.compile(r"^hola$", re.IGNORECASE)), hola))
app_tg.add_handler(MessageHandler(filters.Regex(re.compile(r"^precio$", re.IGNORECASE)), precio))
app_tg.add_handler(MessageHandler(filters.Regex(re.compile(r"^adios?$", re.IGNORECASE)), adios))

app_tg.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, desconocido))
