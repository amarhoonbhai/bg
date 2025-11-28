from aiogram import Router, types
from utils.buttons import start_menu
from utils.check_member import check_all_membership

router = Router()


@router.callback_query()
async def menu_callback(callback: types.CallbackQuery, bot):
    user_id = callback.from_user.id

    # Membership check every time
    ok = await check_all_membership(bot, user_id)
    if not ok:
        from utils.buttons import verify_buttons
        return await callback.message.edit_text(
            "🔐 You must stay joined to continue.",
            reply_markup=verify_buttons()
        )

    if callback.data == "help":
        return await callback.message.answer(
            "🆘 <b>Help Menu</b>\n• Remove BG\n• Enhance HD\n• Auto DP Crop\n• Clean Face"
        )

    if callback.data == "stats":
        return await callback.message.answer("📊 Working perfectly!")

    # Forward actions
    await callback.message.answer(
        "📤 Please send the image now…"
    )

    callback.message.bot.user_action = callback.data
