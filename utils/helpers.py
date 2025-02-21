import os
import time
from typing import Union
from pyrogram import Client
from config import Config
from utils.database import Database

async def is_subscribed(user_id: int) -> bool:
    """Check if user is subscribed to all required channels"""
    if not Config.F_SUB_CHANNELS:
        return True
    
    try:
        for channel in Config.F_SUB_CHANNELS:
            member = await Client.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        return True
    except Exception as e:
        print(f"Subscription check error: {e}")
        return False

async def check_user_limit(user_id: int) -> bool:
    """Check user's daily download limit"""
    db = Database()
    user = await db.users.find_one({"_id": user_id})
    if not user:
        await db.add_user(user_id)
        return True
    return user.get("downloads", 0) < Config.DAILY_LIMIT

def get_file_size(path: str) -> str:
    """Get human-readable file size"""
    size = os.path.getsize(path)
    units = ["B", "KB", "MB", "GB"]
    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} GB"

async def cleanup_files() -> None:
    """Cleanup old downloaded files"""
    try:
        now = time.time()
        for filename in os.listdir("downloads"):
            file_path = os.path.join("downloads", filename)
            if os.path.isfile(file_path):
                if (now - os.stat(file_path).st_mtime) > 3600:  # 1 hour
                    os.remove(file_path)
    except Exception as e:
        print(f"Cleanup error: {e}")

def format_duration(seconds: int) -> str:
    """Convert seconds to HH:MM:SS format"""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"
