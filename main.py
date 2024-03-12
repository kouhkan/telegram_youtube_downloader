import logging

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, Application, ConversationHandler, CommandHandler, MessageHandler, filters

from src.crud.user import get_or_create_user
from src.crud.youtube import get_or_create_youtube
from src.models.base import Base
from src.settings import push_download_into_queue
from src.settings.config import settings
from src.settings.db import engine, db_context

# Config log
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

YOUTUBE = 1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and get youtube link."""
    try:
        with db_context() as db:
            # Add new users to database
            logger.info(f"User ID: {update.message.from_user.id}")
            get_or_create_user(db=db, telegram_id=update.message.from_user.id)
    except Exception as e:
        logger.info(f"{e}")

    await update.message.reply_text(
        "Hi, Enter your YouTube link please😬!"
    )

    return YOUTUBE


async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text.startswith("https://www.youtube") or \
            update.message.text.startswith("https://youtu"):

        try:
            with db_context() as db:
                youtube = get_or_create_youtube(
                    db=db, user_id=update.message.from_user.id, url=update.message.text
                )
                await update.message.reply_text("Please wait to download your file and upload it for you")
                upload_file_path = push_download_into_queue.delay(youtube.url)
                await context.bot.send_document(
                    update.message.chat_id,
                    document=upload_file_path.get(),
                    write_timeout=1000,
                    read_timeout=1000,
                    connect_timeout=120
                )
        except Exception as e:
            logger.info(f"{e}")
    else:
        await update.message.reply_text("Invalid youtube url😖")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create an application
    app = Application.builder().token(settings["TELEGRAM_TOKEN"]).build()

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Add conversation handler
    handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={},
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(handler)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, youtube))

    # Run the bot until the user presses Ctrl-C
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
