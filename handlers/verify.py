from aiogram import Router, types
from utils.check_member import check_all_membership
from utils.buttons import verify_buttons, start_menu

router = Router()


@router.callback_query(lambda c: c.data == "check_verify")
async def verify_callback(callback: types.CallbackQuery, bot):
    user_id = callback.from_user.id

    ok = await check_all_membership(bot, user_id)
    if not ok:
        return await callback.message.edit_text(
            "❌ <b>You haven’t joined all required channels.</b>\nJoin all and tap again.",
            reply_markup=verify_buttons()
        )

    await callback.message.edit_text(
        "✅ <b>Verification successful!</b>\nChoose a tool below:",
        reply_markup=start_menu()
    )
