from aiogram import Router, types
from utils.buttons import main_menu, help_menu

router = Router()

@router.callback_query()
async def menu_handler(call: types.CallbackQuery):
    bot = call.bot
    data = call.data

    if data == "bg":
        bot.user_mode = "bg"
        return await call.message.answer("🧼 <b>Send a photo to remove background.</b>")

    if data == "cutout":
        bot.user_mode = "cutout"
        return await call.message.answer("✂️ <b>Send a photo for smart cut-out.</b>")

    if data == "help":
        return await call.message.answer(
            "<b>🆘 Help Menu</b>\n\n"
            "🧼 Remove BG → Removes background from images\n"
            "✂️ Cut-Out → Smart object extraction\n"
            "📊 Stats → Your usage details\n\n"
            "Send a photo after choosing a tool.",
            reply_markup=help_menu()
        )

    if data == "back":
        return await call.message.answer("⬅️ Back to menu", reply_markup=main_menu())

    if data == "stats":
        return await call.message.answer("/stats")

    if data == "verify":
        return await call.message.answer("/start")
