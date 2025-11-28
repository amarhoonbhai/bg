from aiogram import Router, types, F
from utils.buttons import start_menu, verify_buttons
from utils.check_member import check_all_membership
from utils.database import get_total_stats, get_last_24h_stats, get_all_users

router = Router()

@router.callback_query()
async def menu_callback(callback: types.CallbackQuery, bot):
    user_id = callback.from_user.id

    ok = await check_all_membership(bot, user_id)
    if not ok:
        return await callback.message.edit_text(
            "🔐 You must stay joined to continue.",
            reply_markup=verify_buttons()
        )

    data = callback.data

    # Help
    if data == "help":
        return await callback.message.answer(
            "🆘 <b>Help</b>\n"
            "Choose a tool then send a photo:\n"
            "• 🧼 Remove Background\n"
            "• ✨ Enhance HD\n"
            "• 📸 Auto DP Crop\n"
            "• 🧹 Face Restore"
        )

    # Stats
    if data == "stats":
        total_users = len(get_all_users())
        total = get_total_stats()
        last = get_last_24h_stats()

        msg = f"""
📊 <b>Bot Usage Stats</b>

👥 Total Users: {total_users}
🖼 Total Actions: {total['bg'] + total['enhance'] + total['dp'] + total['face']}

<b>Lifetime Stats:</b>
🧼 BG Remove: {total['bg']}
✨ Enhance: {total['enhance']}
📸 DP Crop: {total['dp']}
🧹 Face Clean: {total['face']}

<b>Last 24 Hours:</b>
BG: {last['bg']} | Enhance: {last['enhance']} | DP: {last['dp']} | Face: {last['face']}
"""

        return await callback.message.answer(msg)

    # Set user's selected action
    bot.user_action = data
    await callback.message.answer("📤 <b>Send your image now…</b>")
