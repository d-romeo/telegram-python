import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Ciao! Sono un bot Railway 🚂")

app.add_handler(CommandHandler("start", start))

app.run_polling()
