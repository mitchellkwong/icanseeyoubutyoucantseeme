from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

class Start:
    command = 'start'
    help_text = 'Get some bot info'

    def __init__(self):
        self.handler = CommandHandler(self.command, self.callback)

    def callback(self, update: Update, context: CallbackContext):
        update.message.reply_markdown(
            '*I can see you but you can\'t see me*\n'
            'Welcome! This bot lets you anonymously send messages to registered bot users. '
            'To start, simply register your telegram username! '
            'You can register and unregister anytime with /register and /unregister. '
        )

class Help:
    command = 'help'
    help_text = 'Shows help'

    def __init__(self):
        self.handler = CommandHandler(self.command, self.callback)

    def callback(self, update: Update, context: CallbackContext):
        update.message.reply_text(context.bot_data['help_text'])