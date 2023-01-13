from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import hello_command
from bot_commands import calc_rational_numbers

app = ApplicationBuilder().token("5833371913:AAHZf7ENL87ZxYMRlz-4JZXq8NA368WlHbs").build()


app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("calc", calc_rational_numbers))

app.run_polling()