from flask import Flask, render_template, redirect, request

app = Flask(__name__)


def main():
    app.run(host="0.0.0.0")
