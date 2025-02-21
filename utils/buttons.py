from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config

def start_markup():
    buttons = [
        [InlineKeyboardButton("📜 Supported Sites", callback_data="sites")],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help")]
    ]
    
    # Add Force Sub buttons
    for channel in Config.F_SUB_CHANNELS:
        buttons.append([InlineKeyboardButton(f"Join Channel", url=f"t.me/{channel}")])
    
    buttons.append([InlineKeyboardButton("👨💻 Developer", url=f"tg://user?id={Config.OWNER_ID}")])
    return InlineKeyboardMarkup(buttons)

def site_list_markup():
    sites = Config.SUPPORTED_SITES
    buttons = []
    row = []
    for i, site in enumerate(sites):
        row.append(InlineKeyboardButton(site.capitalize(), callback_data=f"site_{site}"))
        if (i+1) % 3 == 0:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([InlineKeyboardButton("🔙 Back", callback_data="back")])
    return InlineKeyboardMarkup(buttons)
