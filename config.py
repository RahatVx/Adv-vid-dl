import os

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/VideoBot")
    F_SUB_CHANNELS = [int(x) for x in os.getenv("F_SUB_CHANNELS", "").split(",") if x]
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
    OWNER_ID = int(os.getenv("OWNER_ID"))
    DAILY_LIMIT = int(os.getenv("DAILY_LIMIT", 5))
    FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
    
    SUPPORTED_SITES = [
        "youtube", "tiktok", "instagram", "facebook",
        "twitter", "dailymotion", "terabox", "likee",
        "snackvideo", "rumble", "pinterest"
    ]
