from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu():

    keyboard = [
        [
            KeyboardButton(text="💬 Chat with AI"),
        ],
        [
            KeyboardButton(text="🧠 My Memory"),
            KeyboardButton(text="👤 My Profile"),
        ],
        [
            KeyboardButton(text="⚙️ Settings"),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Ask me anything..."
    )