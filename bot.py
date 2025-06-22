import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Ciao! Sono un bot Railway 🚂")

async def link(update, context):
    await update.message.reply_text("Ecco il link per le prenotazioni! https://calendar.app.google/JAeEMzsJX5yjQQ5N6")

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("link", link))
app.run_polling()
