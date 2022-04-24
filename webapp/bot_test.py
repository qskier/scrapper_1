import logging
import telegram
from telegram.ext import Updater, CommandHandler
from parser import flats

import settings

logging.basicConfig(filename='bot.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s')

def hello(update, context):
    print("Вызван /start", update)
    update.message.reply_text("Добро пожаловать! Если хотите получать ежедневное сообщение о количестве квартир, введите команду /flats")

def flatz(update, context):
    print("Вызван /flats")
    #update.message.reply_text(flats)
    context.job_queue.run_repeating(callback_30, interval=30, first=15) #context=update.message.chat_id)

def now(update, context):
    print("Вызван /now")
    update.message.reply_text(flats)

def callback_30(context: telegram.ext.CallbackContext):
    #chat_id = update.effective_chat.id
    context.bot.send_message(chat_id='30241142', text=flats)
    #(chat_id=update.effective_chat.id, text=flats)
    #context.bot.send_message(chat_id=chat_id, text=flats)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", hello))
    dp.add_handler(CommandHandler("flats", flatz, pass_job_queue=True))
    dp.add_handler(CommandHandler("now", now))

    logging.info("Бот стартовал")
    mybot.start_polling() #регулярные, частые обращения бота к Телеграмму
    mybot.idle() #обращайся к ТГ регулярно, пока тебя не отменят

if __name__ == '__main__':
    main()




#def callback_30(context: telegram.ext.CallbackContext):
    #context.bot.send_message(chat_id='30241142', text=flats)




#j = mybot.job_queue
#job_queue = JobQueue()

#dispatcher = updater.dispatcher