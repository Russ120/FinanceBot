from dotenv import load_dotenv
load_dotenv()

from bot import app_tg

print("Bot local corriendo... (polling)")
app_tg.run_polling()
