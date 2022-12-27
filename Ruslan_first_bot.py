from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
updater = Updater('TOKEN')
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start')
updater.start_polling()
updater.idle()




# from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
# from telegram import Update
# from config import TOKEN
# from anecApi import anecApi

# def Get_calc(update: Update, context: CallbackContext):
#     after_command = context.args
#     update.message.reply_text(anecApi.soviet_joke())
#     print (after_command)

# def Catch_message(update: Update, context: CallbackContext):
#     in_message = update.message.text
#     if 'Прив' in in_message.lower:
#          update.message.reply_text(f'Я Вас НЕНАВИЖУ!!!')
#          return None

#     update.message.reply_text(f'Вы ввели {in_message}')
#     print (in_message)

# updater = Updater(TOKEN)
# dispatcher = updater.dispatcher


# Calc_handler = CommandHandler('start', Get_calc)
# in_message_handler = MessageHandler(Filters.text, Catch_message)

# dispatcher.add_handler(Calc_handler)
# dispatcher.add_handler(in_message_handler)

# print ('Сервер запущен')
# updater.start_polling()
# updater.idle()


