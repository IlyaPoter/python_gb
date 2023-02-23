from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
# import calculate
import user_interfeice
import model_racional as mr



async def my_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    my_text = update.message.text
    example_list = user_interfeice.get_nums(my_text)[1]
    await update.message.reply_text(mr.get_result(example_list))

app = ApplicationBuilder().token("6009724465:AAEaYc3wNiX6UM67u4hHWihY270eSv3vrYM").build()

app.add_handler(MessageHandler(filters.TEXT, my_calc))

app.run_polling()
