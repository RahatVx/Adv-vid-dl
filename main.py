import os
import logging
import asyncio
from threading import Thread
from flask import Flask
from pyrogram import Client
from config import Config
from utils.database import Database
from handlers import start_handler, download_handler, admin_handler

# Initialize Flask
flask_app = Flask(__name__)

@flask_app.route('/')
def health_check():
    return "🚀 Bot is Running | terabox | tiktok | youtube"

class VideoBot(Client):
    def __init__(self):
        super().__init__(
            "AdvancedVideoBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
        )
        self.db = Database()

    async def start(self):
        await super().start()
        logging.info("Bot started with Terabox support!")

def run_flask():
    flask_app.run(host='0.0.0.0', port=Config.FLASK_PORT)

if __name__ == "__main__":
    Thread(target=run_flask, daemon=True).start()
    bot = VideoBot()
    bot.run()
