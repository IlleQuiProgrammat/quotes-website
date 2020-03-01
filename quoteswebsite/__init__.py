from flask import Flask, render_template, redirect, request
from flask_discord import DiscordOAuth2Session
from .constants import DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, \
    DISCORD_REDIRECT_URI, DISCORD_SERVER
from functools import wraps

app = Flask(__name__)
app.secret_key = constants.FLASK_SESSION_SECRET

app.config["DISCORD_CLIENT_ID"] = constants.DISCORD_CLIENT_ID
app.config["DISCORD_CLIENT_SECRET"] = constants.DISCORD_CLIENT_SECRET
app.config["DISCORD_REDIRECT_URI"] = constants.DISCORD_REDIRECT_URI
discord = DiscordOAuth2Session(app)

def verify_user():
    if discord.authorized:
        in_server = False
        guilds = discord.get("/users/@me/guilds")
        for guild in guilds:
            if int(guild["id"]) == constants.DISCORD_SERVER:
                in_server = True
        return in_server
    else:
        return False

def protected_route(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if verify_user():
            return route(*args, **kwargs)
        else:
            return redirect("/login")
    return wrapper

@app.route("/", methods=["GET"])
@protected_route
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def login():
    if verify_user():
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/oauth_redirect", methods=["GET"])
def oauth_redirect():
    return discord.create_session("identify guilds")

@app.route("/oauth_callback", methods=["GET"])
def oauth_callback():
    discord.callback()
    return redirect("/")

@app.route("/logout", methods=["GET"])
def logout():
    if discord.authorized:
        discord.revoke()
    return redirect("/login")

def main():
    app.run(host="0.0.0.0")
