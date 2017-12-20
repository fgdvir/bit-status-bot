from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
updater = Updater(token='463497149:AAEbyWnctU62b0FXFuacMXG_Z8m5pPUCSpc')
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()