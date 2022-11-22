from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [['Приветствие', 'Настоящее время', 'Список операций'],['Сумма', 'Умножение', 'Деление']]
    await update.message.reply_text(
        "Какую кнопку будем нажимать?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            one_time_keyboard=False,
            input_field_placeholder="Ваш выбор?"
        )
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! Добро пожаловать в калькульятор!', start)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/mult\n/division')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')

async def division_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')