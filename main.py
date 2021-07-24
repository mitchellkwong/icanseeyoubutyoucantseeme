import json
import logging

from telegram.ext import Updater, PicklePersistence
from telegram.ext.commandhandler import CommandHandler

logging.basicConfig(
    format='%(asctime)s \t %(name)s \t %(levelname)s \t %(message)s', 
    level=logging.INFO,
)

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Make a bot
    updater = Updater(
        token = config['token'],
        persistence = PicklePersistence('database.p'),
    )

    # Load handlers
    from features.base import Start, Help
    from features.registration import Register, Unregister
    from features.messaging import Forward

    features = [
        Start(),
        Help(),
        Register(),
        Unregister(),
        Forward(),
    ]
    
    for feature in features:
        updater.dispatcher.add_handler(feature.handler)

    # Automatically generate message for /help
    help_text = []
    for feature in features:
        if isinstance(feature.handler, CommandHandler):
            help_text.append(f'/{feature.command}: {feature.help_text}')
    help_text = '\n'.join(help_text)

    # Generate buaya buayee chains
    buayas = dict()
    buayees = dict()
    for chain in config['chains']:
        n = len(chain)
        for i in range(n):
            buaya = chain[i].lower()
            buayee = chain[(i+1)%n].lower() # Chain loops back to start
            buayas[buayee] = buaya # wtf
            buayees[buaya] = buayee # wtf again

    # Update database
    updater.dispatcher.bot_data['help_text'] = help_text
    updater.dispatcher.bot_data['buayas'] = buayas
    updater.dispatcher.bot_data['buayees'] = buayees
    if 'users' not in updater.dispatcher.bot_data:
        updater.dispatcher.bot_data['users'] = dict()

    print('buayas\n', buayas)
    print('buayees\n', buayees)

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
