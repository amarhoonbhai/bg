from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ios_button(text, callback):
    return InlineKeyboardButton(
        text=f"  {text}  ",  # iOS rounded padding
        callback_data=callback
    )


def start_menu():
    kb = [
        [ios_button("🧼 Remove Background", "remove_bg")],
        [ios_button("✨ Enhance HD (4x)", "enhance_hd")],
        [ios_button("📸 Auto DP Crop", "dp_crop")],
        [ios_button("🧹 Face Restore", "clean_face")],
        [
            ios_button("📑 Help", "help"),
            ios_button("📈 Stats", "stats")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def verify_buttons():
    kb = [
        [InlineKeyboardButton("📌 Join @PhiloBots", url="https://t.me/PhiloBots")],
        [InlineKeyboardButton("📌 Join @TheTrafficZone", url="https://t.me/TheTrafficZone")],
        [InlineKeyboardButton("📌 Join @ClaimBack", url="https://t.me/ClaimBack")],
        [InlineKeyboardButton("📌 Join Group Chat", url="https://t.me/+X83tuZcK0FkwZWY1")],
        [ios_button("🔁 I Joined", "check_verify")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)
