import telegram # importamos las librerias  
import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from TokenManager import TokenManager

TOKEN = TokenManager.getToken('text_files/secured_token.txt')

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# To know when things dont work as expected 
LOG_FILE = 'text_files/lost_err.txt';
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

# Functions that contains the actions of the commands when they are pressed
def start(bot, update):
     bot.send_message(chat_id=update.message.chat_id, 
                      text='<b>Lost Wiki</b>.\r\nHere you can find information about the show.',
                      parse_mode=telegram.ParseMode.HTML)
     bot.send_photo(chat_id=update.message.chat_id, photo=open('img/lost1.png', 'rb'))

def character(bot, update): 
     bot.send_message(chat_id=update.message.chat_id, 
                      text='<a href="http://es.lostpedia.wikia.com/wiki/Portal:Personajes_Principales">Main Characters</a>',
                      parse_mode=telegram.ParseMode.HTML)

def description(bot, update):
     bot.send_message(chat_id=update.message.chat_id,
                      text='<a href="http://telegram.me/Lost815Bot">Bot description</a>',
                      parse_mode=telegram.ParseMode.HTML)

def strange(bot, update):
     bot.send_message(chat_id=update.message.chat_id,
                      text='<a href="http://es.lostpedia.wikia.com/wiki/Portal:Misterios">Weird Events in Lost</a>',
                      parse_mode=telegram.ParseMode.HTML)

def places(bot, update):
     bot.send_message(chat_id=update.message.chat_id,
                      text='<a href="http://es.lostpedia.wikia.com/wiki/Portal:Lugares">Places</a>',
                      parse_mode=telegram.ParseMode.HTML)

def seasons(bot, update):
     bot.send_message(chat_id=update.message.chat_id,
                      text='<a href="http://es.lostpedia.wikia.com/wiki/Portal:Episodios">Seasons</a>',
                      parse_mode=telegram.ParseMode.HTML)

def unknown(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


# Exec the commands
handlers = [
     CommandHandler('start', start), 
     CommandHandler('character', character),
     CommandHandler('desc', description),
     CommandHandler('strange', strange),
     CommandHandler('places', places),
     CommandHandler('season', seasons),
     MessageHandler(Filters.command, unknown)
]

def main(list):
     for handler in list: 
	try:
            dispatcher.add_handler(handler)
     	except Exception as err:
            logger.error(err)

if __name__ == '__main__':
    main(handlers)
    updater.start_polling()
