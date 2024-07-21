import argparse
import sys

from flask import Flask, request
from telegram import Update
from dotenv import load_dotenv

from dispatcher import dispatcher, bot

load_dotenv()

app = Flask(__name__)


@app.route('/webhook/', methods=['POST'])
def webhook() -> str:
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Telegram Bot with Webhook')
    parser.add_argument('--webhook', type=str, help='Webhook URL')
    parser.add_argument('--port', type=int, default=4500, help='Port number (default: 4500)')
    args = parser.parse_args()

    if args.webhook:
        bot.set_webhook(url=args.webhook)
        sys.stdout.write(f"Webhook set to: {args.webhook}")

    # Run Flask app
    app.run(port=args.port)