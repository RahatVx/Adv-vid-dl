import yt_dlp
import os
from pyrogram.types import Message
from config import Config
from utils.helpers import (
    is_subscribed,
    check_user_limit,
    get_file_size,
    cleanup_files
)
from utils.progress import progress_callback

async def handle(client, message: Message):
    user = message.from_user
    try:
        if not await is_subscribed(user.id):
            return await message.reply("❌ Join our channels first!")
        
        if not await check_user_limit(user.id):
            return await message.reply(f"⚠️ Daily limit: {Config.DAILY_LIMIT}")

        url = message.text.split(" ", 1)[1]
        msg = await message.reply("🔍 Processing...")

        ydl_opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "progress_hooks": [lambda d: progress_callback(d, msg)],
            "noplaylist": True,
        }

        # Terabox specific configuration
        if "terabox" in url:
            ydl_opts.update({
                "http_headers": {
                    "Cookie": "ndus=YOUR_TERABOX_COOKIE",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                },
                "format": "bestvideo+bestaudio/best",
            })
        elif "tiktok" in url:
            ydl_opts["extractor_args"] = {"tiktok": {"watermark": False}}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            
            await msg.edit("📤 Uploading...")
            await message.reply_video(
                file_path,
                caption=f"🎬 {info.get('title', 'Video')}\n💾 {get_file_size(file_path)}",
                progress=progress_callback,
                progress_args=(msg,)
            )
            
            await client.db.update_user(user.id)
            await client.send_message(
                Config.LOG_CHANNEL,
                f"📥 Downloaded: {url}\n👤 User: {user.mention}"
            )

    except Exception as e:
        await msg.edit(f"❌ Error: {str(e)}")
    finally:
        await cleanup_files()
