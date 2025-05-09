from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_bot():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text="royhadan otish", callback_data="register_bot")
    )
    return markup
