from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import sys

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("Errore: la variabile TELEGRAM_TOKEN non è impostata.", file=sys.stderr)
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono un bot Telegram su Render!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("Bot in esecuzione...")
    app.run_polling()
