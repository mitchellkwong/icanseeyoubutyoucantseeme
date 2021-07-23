# 👁👄👁 icanseeyoubutyoucantseeme

This telegram bot allows registered users to send anonymized messages to other registered users.
It was primarily designed to ease the workload for commitees running "Angel and Mortal" styled 
games and includes specific features geared towards this.

## Features

**Anonymous Messaging**
Message other registered users with `@username <message>`: The registered user will only receive `<message>`.

**Automatic Aliasing**
Users can be set up into loops where they can message the next person in the loop with `@buayee <message>` 
and the previous person in the loop with `@buaya <message>`.

## Dependencies & Setup

The project runs on python 3.? and uses the `python-telegram-bot` package. Grab it with:

```pip install python-telegram-bot```

Additionally, you will need to provide a telegram bot token in `config.json`. 
User loops can also be defined in this file (refer to `config.json.example`).
