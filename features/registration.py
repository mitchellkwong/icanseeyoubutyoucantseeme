from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    commandhandler,
)

class Register:
    command = 'register'
    help_text = 'Add your username from our records to message other users'

    def __init__(self):
        self.handler = CommandHandler(self.command, self.callback)

    def callback(self, update: Update, context: CallbackContext):
        user = update.effective_user.name
        chat = update.message.chat_id
        context.bot_data['users'][user] = chat
        update.message.reply_markdown(
            'Your username has been recorded! '
            f'You can now anonymously message other registered users with "@username message" (e.g.: "`{user} Hello me!`"). '
            'Use /unregister to remove yourself from the records.'
        )

class Unregister:
    command = 'unregister'
    help_text = 'Removes your username from our records'

    def __init__(self):
        self.handler = CommandHandler(self.command, self.callback)

    def callback(self, update: Update, context: CallbackContext):
        user = update.effective_user
        del context.bot_data['users'][user.name]
        update.message.reply_text(
            f'Your username has been removed from the records. '
            'Use /start if you\'d like to register again.'
        )