#!/usr/bin/python3.6
''' pubg report bot'''

import discord, logging
from bot.main import client as client
logging.basicConfig(level=logging.DEBUG)

# Create an API key here: https://discordapp.com/developers/applications/
# Create a webhook in the channel settings of your discord server
bot_token = 'ae1829e64a7f85014f61900d1b29724f07062197c72a32e494738f7429e6b716' # Bot token (discordapi)
webhook_uri = 'https://discord.com/api/webhooks/955479589507973260/uQzJqrAnDzGSszhb5ExSMKzvYOaLJQ-SJx7Kzd6XTLIn_qb5sj61q_ezi-DsbBuOjxfY' #Webhook URL (discord client)

check_rate = 12  # How often the bot will check for updates, in minutes (no less than five minutes or you'll be banned from pubg.report)
if __name__ == "__main__":
    client.run(bot_token)
