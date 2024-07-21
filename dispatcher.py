from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler

from handlers import commands, common
import states
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('start', commands.start)],
    states={
        states.NAME: [
            MessageHandler(Filters.text, common.get_name),
            MessageHandler(Filters.photo, common.invalid_name),
            MessageHandler(Filters.document, common.invalid_name),
            MessageHandler(Filters.voice, common.invalid_name),
            MessageHandler(Filters.video, common.invalid_name),
            MessageHandler(Filters.location, common.invalid_name),
        ],
        states.AGE: [
            MessageHandler(Filters.text, common.get_age),
            MessageHandler(Filters.photo, common.invalid_age),
            MessageHandler(Filters.document, common.invalid_age),
            MessageHandler(Filters.voice, common.invalid_age),
            MessageHandler(Filters.video, common.invalid_age),
            MessageHandler(Filters.location, common.invalid_age),
        ],
        states.GENDER: [
            MessageHandler(Filters.text, common.get_gender),
            MessageHandler(Filters.photo, common.invalid_gender),
            MessageHandler(Filters.document, common.invalid_gender),
            MessageHandler(Filters.voice, common.invalid_gender),
            MessageHandler(Filters.video, common.invalid_gender),
            MessageHandler(Filters.location, common.invalid_gender),
        ],
        states.ADDRESS: [
            MessageHandler(Filters.text, common.get_address),
            MessageHandler(Filters.photo, common.invalid_address),
            MessageHandler(Filters.document, common.invalid_address),
            MessageHandler(Filters.voice, common.invalid_address),
            MessageHandler(Filters.video, common.invalid_address),
            MessageHandler(Filters.location, common.invalid_address),
        ]
    },
    fallbacks=[commands.error]
))

dispatcher.add_handler(MessageHandler(Filters.text, common.echo))

# dispatcher.add_handler(CommandHandler("start", commands.start))
# dispatcher.add_handler(CommandHandler("help", commands.help))
# dispatcher.add_handler(CommandHandler("subscribe", commands.subscribe))
# dispatcher.add_handler(CommandHandler("info", commands.info))
