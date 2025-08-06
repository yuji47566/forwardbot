from pyrogram import Client, filters
from pyrogram.types import Message

# Bot configuration
api_id = 27592456  # replace with your API ID
api_hash = "f1ef056e23af66e607a352c1b62df7e5"  # replace with your API HASH
bot_token = "7846862935:AAEN7E4TlI1Sv4rzVzafSx-oEXLlwM8Utf0"  # replace with your Bot Token

source_channel = -1002700401348  # Source channel ID
destination_channel = -1002510315345  # Destination channel ID

# Image and Welcome Text
welcome_image_url = "https://files.catbox.moe/n03hsx.jpg"  # Use https://telegra.ph to upload image
welcome_text = """
👋 Welcome to the Forward Bot!

📢 This bot automatically forwards posts from our main channel.

👨‍💻 Developed by: @Mr_Kevin_Official
🔗 Channel: @MovieZone_Era
"""

app = Client("forward_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# 1️⃣ START command handler with button
@app.on_message(filters.private & filters.command("start"))
async def start_cmd(client, message: Message):
    buttons = [[
        {"text": "🔗 Join Developer Channel", "url": "https://t.me/MoviesZone_Era"}
    ]]
    await message.reply_photo(
        photo=welcome_image_url,
        caption=welcome_text,
        reply_markup={"inline_keyboard": buttons}
    )

# 2️⃣ Forward messages from source to destination
@app.on_message(filters.channel & filters.chat(source_channel))
async def forward_handler(client, message: Message):
    await message.copy(destination_channel)

app.run()