from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_gender_keyboard():
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Male"), KeyboardButton(text="Female")
            ],
            [
                KeyboardButton(text="Ortga")
            ]
        ]
    )
