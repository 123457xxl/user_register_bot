import handlers

from config.bot import bot

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.polling(none_stop=True)

