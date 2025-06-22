import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === Percorso file per salvare utenti ===
USER_FILE = os.path.join(os.path.dirname(__file__), "utenti.json")


# === Carica utenti da file ===
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# === Salva utenti su file ===
def save_users():
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=2, ensure_ascii=False)

# === Inizializza ===
TOKEN = os.environ.get("TELEGRAM_TOKEN")
user_data = load_users()

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = str(update.effective_chat.id)  # chiave stringa per JSON

    # Salva l'utente
    user_data[chat_id] = {
        "first_name": user.first_name,
        "username": user.username,
        "id": user.id,
    }
    save_users()

    keyboard = [
        [InlineKeyboardButton("📅 Prenota", url="https://calendar.app.google/")],
        [InlineKeyboardButton("💻 GitHub", url="https://github.com/d-romeo")],
        [InlineKeyboardButton("📬 Contattami", url="https://t.me/@dromeo_1")]
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

# === /link ===
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Prenota qui: https://calendar.app.google/JAeEMzsJX5yjQQ5N6")

# === /utenti ===
async def utenti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not user_data:
        await update.message.reply_text("Nessun utente ha ancora usato il bot.")
        return

    msg = "📋 Utenti registrati:\n"
    for u in user_data.values():
        msg += f"• {u['first_name']} (@{u['username']})\n"
    await update.message.reply_text(msg)

# === App ===
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("link", link))
app.add_handler(CommandHandler("utenti", utenti))

app.run_polling()
