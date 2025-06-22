import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Prendi il token da variabili ambiente
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Dizionario per salvare gli utenti che usano il bot
user_data = {}

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Salva utente
    user_data[chat_id] = {
        "first_name": user.first_name,
        "username": user.username,
        "id": user.id,
    }

    keyboard = [
        [InlineKeyboardButton("📅 Prenota", url="https://calendar.app.google/JAeEMzsJX5yjQQ5N6")],
        [InlineKeyboardButton("💻 GitHub", url="https://github.com/TUO_USERNAME")],
        [InlineKeyboardButton("📬 Contattami", url="https://t.me/TUO_USERNAME")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Ciao {user.first_name}! 👋\n\n"
        "Sono il tuo bot personale. Puoi:\n"
        "• Prenotare una lezione\n"
        "• Visitare il mio GitHub\n"
        "• Contattarmi direttamente",
        reply_markup=reply_markup
    )

# === /link (comando extra diretto) ===
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Prenota qui: https://calendar.app.google/JAeEMzsJX5yjQQ5N6")

# === /utenti (debug: mostra utenti registrati) ===
async def utenti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not user_data:
        await update.message.reply_text("Nessun utente ha ancora usato il bot.")
        return

    msg = "📋 Utenti registrati:\n"
    for u in user_data.values():
        msg += f"• {u['first_name']} (@{u['username']})\n"
    await update.message.reply_text(msg)

# === Build app ===
app = ApplicationBuilder().token(TOKEN).build()

# === Handler comandi ===
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("link", link))
app.add_handler(CommandHandler("utenti", utenti))

# === Avvia il bot ===
app.run_polling()
