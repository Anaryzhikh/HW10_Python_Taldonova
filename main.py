import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from bot_commands import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = ApplicationBuilder().token('').build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('mult', mult_command))
app.add_handler(CommandHandler('division', division_command))

msg = MessageHandler(filters.TEXT, lambda msg: print(msg))
app.add_handler(msg)

print('server start')
app.run_polling()
app.idle()