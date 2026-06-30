import os
import asyncio
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Web Server for Render Health Checks ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"TraderHub Education Bot Is Active!")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

def run_health_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    print(f"Health check server running on port {port}")
    server.serve_forever()

# --- Core Event Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    
    await update.message.reply_text(
        text=welcome_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def main():
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    if not TOKEN:
        raise ValueError("Missing TELEGRAM_TOKEN parameter inside environment variables.")

    threading.Thread(target=run_health_server, daemon=True).start()

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("TraderHub Educational bot framework actively polling...")
    
    async with app:
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        while True:
            await asyncio.sleep(3600)

# --- THE CRITICAL FIX ---
if name == "__main__":
    asyncio.run(main())
