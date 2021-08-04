import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', 8443))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1906828102:AAFpGRVV5t27ywJnV8C4oELGrf37qRo8nRI'

def start(update, context):
    update.message.reply_text('Hi!')

def help(update, context):
    update.message.reply_text("'Сергей', 'Эльдар', 'усы', 'Бала', 'Бала привет', 'ты как', 'заткните его', 'пизды дам'")


def echo(update, context):
    user_says = update.message.text.lower().split()
    for user_say in user_says:
        if "сергей" in user_say:
            update.message.reply_text("@MarkSulla, ты работу нашел?")
    	elif "эльдар" in user_say:
            update.message.reply_text("привет бала")
    	elif "усы" in user_say:
            update.message.reply_text("@MarkSulla усы побрил?")
    	elif user_say == "бала":
            update.message.reply_text("что брат?")
    	elif user_say == "бала привет":
            update.message.reply_text("Привет брат")
    	elif "ты как" in user_say:
            update.message.reply_text("Пойдет брат, ты как?")
    	elif "заткните его" in user_say:
            update.message.reply_text("Слава Казахстану, героям слава")
    	elif "пизды дам" in user_say:
            update.message.reply_text("https://t.me/c/1552294756/1821")
	elif "user_says" in user_say:
	    update.message.reply_text(user_say)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen = "0.0.0.0", 
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url='https://stormy-thicket-52208.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()