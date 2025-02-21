from pyrogram.types import Message
from utils.database import Database

async def handle_stats(client, message: Message):
    db = Database()
    total_users = await db.total_users()
    total_downloads = await db.total_downloads()
    await message.reply_text(
        f"📊 **Bot Statistics**\n\n"
        f"👥 Total Users: `{total_users}`\n"
        f"📥 Total Downloads: `{total_downloads}`\n"
        f"🔔 Daily Limit: `{Config.DAILY_LIMIT}`/user"
    )

async def handle_broadcast(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to broadcast")
    
    users = await Database().get_all_users()
    success = 0
    for user in users:
        try:
            await client.copy_message(
                chat_id=user['_id'],
                from_chat_id=message.chat.id,
                message_id=message.reply_to_message.id
            )
            success += 1
        except Exception as e:
            print(f"Broadcast error: {e}")
    await message.reply_text(f"Broadcast sent to {success}/{len(users)} users")
