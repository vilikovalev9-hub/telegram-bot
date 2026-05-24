
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8296456401:AAGVF0Zk6rd8I9PFaD9C0FbQM0ZP3ZX4WN8"
ADMIN_ID = 7785097021

keyboard = ReplyKeyboardMarkup(
    [["👤 Профиль"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот запущен 24/7 👋", reply_markup=keyboard)

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"ID: {user.id}\nUsername: @{user.username}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "👤 Профиль":
        await profile(update, context)
    else:
        await update.message.reply_text(update.message.text)

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot running...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
