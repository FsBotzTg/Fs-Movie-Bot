from pyrogram import Client, filters, enums
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton


@Client.on_message(filters.command("button"))
async def button(client, message):
    await message.react(emoji="🎉")
    # Create buttons
    button1 = KeyboardButton("/start")
    button2 = KeyboardButton("/admin")
    button3 = KeyboardButton("/stats")
    button4 = KeyboardButton("/stream")
    button5 = KeyboardButton("/format")

    # Create keyboard layout (2x1 grid)
    keyboard = [[button1], [button2], [button3], [button4], [button5]]

    # Create reply markup
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Send message with keyboard
    await message.reply_text("<b>Buttons Activated 🥳<b>", reply_markup=reply_markup)