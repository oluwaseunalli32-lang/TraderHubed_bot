import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Core Event Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 👇 CHANGE 'YOUR_GITHUB_USERNAME' TO YOUR ACTUAL GITHUB ACCOUNT USERNAME:
    WELCOME_IMAGE_URL = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/traderhub-education-bot/main/welcome.jpg"

    welcome_text = (
        "📈 **Welcome to TraderHub Education.**\n\n"
        "This channel is dedicated to educational content related to financial markets, "
        "market structure, risk management, trading psychology, and trading methodologies.\n\n"
        "Our goal is to provide learning resources that help individuals better understand "
        "how financial markets operate through educational materials, market analysis examples, "
        "and trading concepts.\n\n"
        "Topics discussed may include Forex, Gold (XAUUSD), price action, supply and demand, "
        "market structure, and risk management principles. Content is intended for educational "
        "and informational purposes only.\n\n"
        "TraderHub Education does not provide investment advice, trading signals, financial "
        "recommendations, or guarantees of any kind. All information shared is designed solely "
        "to support learning and personal research.\n\n"
        "By joining this channel, you acknowledge that any decisions related to financial markets "
        "remain your own responsibility.\n\n"
        "Thank you for joining TraderHub Education. ✨"
    )
    
    keyboard = [
        [InlineKeyboardButton("📢 Join TraderHub Education Channel", url="https://t.me/TraderHub_Education")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Sends your image along with your welcome layout text neatly pinned below it
    await update.message.reply_photo(
        photo=WELCOME_IMAGE_URL,
        caption=welcome_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def main():
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    if not TOKEN:
        raise ValueError("Missing TELEGRAM_TOKEN parameter inside environment variables.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("TraderHub Educational bot framework actively polling as a Background Worker...")
    
    async with app:
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        while True:
            await asyncio.sleep(3600)

# --- DIRECT EXECUTION RUNNER WITH NO TYPO-PRONE IF STATEMENTS ---
asyncio.run(main())
