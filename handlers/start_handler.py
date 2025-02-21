from pyrogram.types import Message
from utils.buttons import start_markup
from config import Config

async def handle(client, message: Message):
    user = message.from_user
    text = f"""
    🚀 **Welcome {user.mention}!**

    📌 **Features:**
    - 50+ Supported Sites (Including Terabox)
    - 4K/HD Quality
    - Fast Download Speed
    - Daily Limit: {Config.DAILY_LIMIT}/day
    
    🔧 **How to Use:**
    Send /download followed by URL
    Example: `/download https://terabox.com/...`

    📌 **Note:** For Terabox links, ensure you're using valid public links
    """
    
    await message.reply_text(
        text,
        reply_markup=start_markup(),
        disable_web_page_preview=True
    )
