from aiogram import Router, types, F
from utils.check_member import check_all_membership
from utils.buttons import verify_buttons, start_menu

router = Router()

@router.callback_query(F.data == "check_verify")
async def verify_callback(callback: types.CallbackQuery, bot):
    user_id = callback.from_user.id

    ok = await check_all_membership(bot, user_id)
    if not ok:
        return await callback.message.edit_text(
            "❌ You still haven’t joined all channels.\nJoin all & tap again.",
            reply_markup=verify_buttons()
        )

    await callback.message.edit_text(
        "✅ Verification complete!\nChoose a tool below:",
        reply_markup=start_menu()
    )
