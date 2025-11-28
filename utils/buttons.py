from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="🧼 Remove BG", callback_data="mode_bg")
    kb.button(text="✂️ Cut-Out", callback_data="mode_cutout")
    kb.button(text="📊 Stats", callback_data="show_stats")
    kb.button(text="ℹ️ Help", callback_data="show_help")
    kb.adjust(2)
    return kb.as_markup()


def verify_button():
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ I Joined", callback_data="verify_join")
    return kb.as_markup()


def back_button():
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Back", callback_data="back_to_menu")
    return kb.as_markup()
