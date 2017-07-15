import telegram # importamos las librerias  
import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep

TOKEN = '417858009:AAHFYd2NkF3TtSHfi5wOoy4kOrismsquTYs'

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# To know when things dont work as expected 
LOG_FILE = 'lost_err.txt';
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

# Functions that contains the actions of the commands when they are pressed
def start(bot, update):
     bot.send_message(chat_id=update.message.chat_id, 
                      text='<b>Lost Wiki</b>.\r\nHere you can find information about the show.',
                      parse_mode=telegram.ParseMode.HTML)
     bot.send_photo(chat_id=update.message.chat_id, photo=open('img/lost1.png', 'rb'))

def unknown(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

handlers = [
     CommandHandler('start', start), 
     MessageHandler(Filters.command, unknown)
]

for handler in handlers: 
     try:
     	dispatcher.add_handler(handler)
     except Exception as err: 
	logger.error(err)

updater.start_polling()
