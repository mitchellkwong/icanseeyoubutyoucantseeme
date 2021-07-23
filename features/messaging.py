import re
from telegram import Update
from telegram.ext import (
    CallbackContext,
    MessageHandler,
    Filters,
)

class Forward:
    pattern = re.compile('^(@\S+) +(.+)$') # Matches "@username message" message formats

    def __init__(self):
        self.handler = MessageHandler(Filters.regex(self.pattern), self.callback)
    
    def callback(self, update: Update, context: CallbackContext):
        sender = update.effective_user.name
        match = self.pattern.match(update.message.text)
        user = match.group(1)
        text = match.group(2)
        
        # Handle unregistered users
        if sender not in context.bot_data['users']:
            update.message.reply_text('/register to send messages through me!')
            return

        # For buayabuayee, antialias the reciever
        if user == '@buaya':
            receiver = context.bot_data['buayas'].get(sender, None)
        elif user == '@buayee':
            receiver = context.bot_data['buayees'].get(sender, None)
        else:
            receiver = user
        
        user_id = context.bot_data['users'].get(receiver, None)

        # For buayabuayee, alias the sender
        if user in '@buaya@buayee':
            sender = '@buaya@buayee'.replace(user, '')
            text = f'{sender}:\n{text}'

        # Forward message
        if user_id is not None:
            try:
                context.bot.send_message(user_id, text)
                update.message.reply_text(f'Sent message to {user}!')
            except Exception as e:
                update.message.reply_text(f'Something went wrong!')
                update.message.reply_text(str(e))
        else:
            update.message.reply_text(
                f'Sorry {user} is not a registered user! '
                f'(You can file a ticket to resolve this issue to {user})'
            )