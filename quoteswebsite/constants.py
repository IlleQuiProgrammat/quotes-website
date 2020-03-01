from os import environ
import random
import string

def random_string(length):
    r = ""
    for i in range(16):
        r += random.choice(string.printable)
        return r

DISCORD_CLIENT_ID = int(environ.get("DISCORD_CLIENT_ID"))
DISCORD_CLIENT_SECRET = environ.get("DISCORD_CLIENT_SECRET")
DISCORD_REDIRECT_URI = environ.get("DISCORD_REDIRECT_URI", "https://quotes.cyberdiscoverycommunity.uk/oauth_callback")
FLASK_SESSION_SECRET = environ.get("FLASK_SESSION_SECRET", random_string(16))

DISCORD_BOT_TOKEN = environ.get("DISCORD_BOT_TOKEN")
DISCORD_SERVER = int(environ.get("DISCORD_SERVER", 409851296116375565))
DISCORD_QUOTES_CHANNEL = int(environ.get("DISCORD_QUOTES_CHANNEL", 463657120441696256))