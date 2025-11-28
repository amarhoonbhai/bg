from aiogram import Router, types
from utils.buttons import main_menu, back_button

router = Router()


@router.callback_query()
async def menu_handler(call: types.CallbackQuery, bot):
    data = call.data

    if data == "mode_bg":
        bot.user_mode = "bg"
        return await call.message.edit_text("🧼 <b>Send a photo to remove background.</b>")

    if data == "mode_cutout":
        bot.user_mode = "cutout"
        return await call.message.edit_text("✂️ <b>Send a photo for smart cut-out.</b>")

    if data == "show_help":
        help_text = """
<b>🆘 Help Menu</b>

🧼 <b>Remove BG</b> → Removes background from images  
✂️ <b>Cut-Out</b> → Extracts object smartly  
📊 <b>Stats</b> → View bot usage  

Send an image after selecting a tool.
"""
        return await call.message.edit_text(help_text, reply_markup=back_button())

    if data == "back_to_menu":
        return await call.message.edit_text("⬅️ Back to menu", reply_markup=main_menu())

    if data == "show_stats":
        return await call.message.answer("/stats")

    if data == "verify_join":
        return await call.message.answer("/start")
