from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from spy import log

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() #sum 123 12345
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def calc_rational_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    log(update, context) 

    msg = update.message.text
    items = msg.split() #calc 123 12345
    x = int(items[1])
    action = items[2]
    y = int(items[3])
    if action == '+':
        await update.message.reply_text(f'{x} + {y} = {x + y}')
    if action == '-':
        await update.message.reply_text(f'{x} - {y} = {x - y}')
    if action == '*':
        await update.message.reply_text(f'{x} * {y} = {x * y}')
    if action == '/':
        await update.message.reply_text(f'{x} / {y} = {x / y}')
    if action == '%':
        await update.message.reply_text(f'{x} % {y} = {x % y}')
