import telegram # importamos las librerias 

TOKEN = '417858009:AAHFYd2NkF3TtSHfi5wOoy4kOrismsquTYs'

bot = telegram.Bot(token=TOKEN)

updates = bot.get_updates()

def updateslist():
	chat_id = bot.get_updates()[-1].message.chat_id
	for u in updates: 
		if u.message.text == "Hurley": 
			bot.send_message(chat_id=chat_id, text="QUE PASO HURLEY!")
		elif u.message.text == "Vicent": 
			bot.send_message(chat_id=chat_id, text="BIcent el de las judias magicas")
print([u.message.text for u in updates])
updateslist()

print chat_id
