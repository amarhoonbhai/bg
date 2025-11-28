from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="🧼 Remove BG", callback_data="bg")
    kb.button(text="✂️ Cut-Out", callback_data="cutout")
    kb.button(text="ℹ️ Help", callback_data="help")
    kb.button(text="📊 Stats", callback_data="stats")
    kb.adjust(2)
    return kb.as_markup()


def verify_button():
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ I Joined", callback_data="verify")
    return kb.as_markup()


def help_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Back", callback_data="back")
    return kb.as_markup()
