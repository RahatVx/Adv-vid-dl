# Advanced Video Downloader Bot 🚀

A feature-rich Telegram bot for downloading videos from 50+ platforms including Terabox, TikTok, YouTube and more.

![Demo](https://img.shields.io/badge/Status-Active-brightgreen) 
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0%2B-orange)

## Features ✨

- ✅ Terabox Download Support (with cookie)
- ✅ TikTok Without Watermark
- ✅ 4K/HD Quality Support
- ✅ Multi-Platform Download
- ✅ Daily Download Limit
- ✅ Force Subscription
- ✅ Auto File Cleanup
- ✅ Progress Tracking
- ✅ Admin Controls

## Setup ⚙️

### Prerequisites
- Python 3.10+
- MongoDB
- FFmpeg
- Telegram API Keys

### Environment Variables
Create `.env` file:
```env
API_ID=1234567
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_URI=mongodb://localhost:27017
F_SUB_CHANNELS=-100123,-100456
LOG_CHANNEL=-100789
OWNER_ID=123456789
DAILY_LIMIT=5
TERABOX_COOKIE=ndus=your_cookie_here
