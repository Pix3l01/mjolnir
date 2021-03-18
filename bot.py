import json
from pathlib import Path

from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
)

bad_words = Path("bad_words.txt").read_text()
bad_words = map(lambda l: l.strip(), bad_words.splitlines())
bad_words = list(bad_words)


def get_token() -> None:
    """Finds the key that leads to the hammer"""

    content = Path("keys.json").read_text()
    dictified = json.loads(content)
    return dictified["TELEGRAM_TOKEN"]


def start(update: Update, _: CallbackContext) -> None:
    """Fear the rage of the hammer"""

    update.message.reply_html(
        "<b>Fear the rage of the hammer!</b>",
        reply_to_message_id=update.message.message_id,
    )


def hammer_cmd(update: Update, _: CallbackContext) -> None:
    """Only a fool could looks for the hammer's rage"""

    update.message.reply_text("🔨😠", reply_to_message_id=update.message.message_id)


def hammer(update: Update, _: CallbackContext) -> None:
    """Whom who insult the hammer should expect his rage"""

    message_id = update.message.message_id
    message_text = update.message.text

    for word in bad_words:
        if message_text.find(word) != -1:
            update.message.reply_text("🔨😠", reply_to_message_id=message_id)
            return


def main() -> None:
    """Start the bot"""

    up = Updater(get_token())

    up.dispatcher.add_handler(CommandHandler("start", start))
    up.dispatcher.add_handler(CommandHandler("help", start))
    up.dispatcher.add_handler(CommandHandler("hammer", hammer_cmd))

    up.dispatcher.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command,
            hammer,
        )
    )

    up.start_polling()
    up.idle()


if __name__ == "__main__":
    main()
