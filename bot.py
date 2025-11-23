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
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# Inicializar el bot de Telegram
app_tg = Application.builder().token(TOKEN).build()


# ======================
#   CHATGPT FUNCION
# ======================
async def chatgpt_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # GRATIS
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ======================
#   HANDLERS NORMALES
# ======================
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos:\n/start\n/help\n/precio\n/investigar")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Usa /investigar para preguntarle cosas a la IA.")

async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Holaaa! 😎")

async def precio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("El precio de hoy es RD$499 (demo)")

async def adios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Nos vemos bro! 👋")


# ======================
#   MODO INVESTIGAR
# ======================
async def investigar_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["modo_investigar"] = True
    await update.message.reply_text("¿Qué quieres investigar, bro?")


async def procesar_investigacion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pregunta = update.message.text
    respuesta = await chatgpt_response(pregunta)
    await update.message.reply_text(respuesta)
    context.user_data["modo_investigar"] = False


# ======================
#   MENSAJE DESCONOCIDO O NORMAL
# ======================
async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Si está en modo investigar → mandar a ChatGPT
    if context.user_data.get("modo_investigar") == True:
        await procesar_investigacion(update, context)
        return

    # Respuestas simples
    text = update.message.text.lower()

    if "hola" in text:
        await hola(update, context)
    elif "precio" in text:
        await precio(update, context)
    elif "adios" in text or "bye" in text:
        await adios(update, context)
    else:
        await update.message.reply_text("No te entendí bro. Usa /investigar para la IA.")


# ======================
#   REGISTRAR HANDLERS
# ======================
app_tg.add_handler(CommandHandler("help", help_cmd))
app_tg.add_handler(CommandHandler("start", start))
app_tg.add_handler(CommandHandler("precio", precio))
app_tg.add_handler(CommandHandler("investigar", investigar_cmd))

app_tg.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
