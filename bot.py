import logging
from telegram.ext import Updater, CommandHandler
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print("start")
    update.message.reply_text("Привет, Сереженька! Я подготовила для тебя интересного бота, который поможет тебе выбирать вкусную еду каждый день! Сначала подпишись на рассылку, чтобы получать уведомления от бота, а после исследуй его возможности.")

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

