from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands

if __name__ == '__main__':
    # bot.stop_bot()
    set_default_commands(bot)
    # bot.infinity_polling()
    bot.polling(none_stop=True)
