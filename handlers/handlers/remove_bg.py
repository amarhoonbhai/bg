from aiogram import Router, types
from utils.check_member import check_all_membership
from services.background import remove_background

router = Router()


@router.message(lambda m: m.photo)
async def handle_image(message: types.Message, bot):
    action = getattr(bot, "user_action", None)
    if not action:
        return

    user_id = message.from_user.id
    ok = await check_all_membership(bot, user_id)
    if not ok:
        from utils.buttons import verify_buttons
        return await message.answer("🔐 Please join all channels.", reply_markup=verify_buttons())

    file = await bot.get_file(message.photo[-1].file_id)
    img = await bot.download_file(file.file_path)

    if action == "remove_bg":
        output = remove_background(img.read())
        await message.answer_photo(
            photo=output,
            caption="🧼 Background Removed!"
        )
