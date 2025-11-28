from aiogram import Router, types
from services.enhance import upscale_image
from utils.check_member import check_all_membership

router = Router()


@router.message(lambda m: m.photo)
async def enhance_handler(message: types.Message, bot):
    action = getattr(bot, "user_action", None)
    if action != "enhance_hd":
        return

    user_id = message.from_user.id
    ok = await check_all_membership(bot, user_id)
    if not ok:
        from utils.buttons import verify_buttons
        return await message.answer("🔐 Please join all channels.", reply_markup=verify_buttons())

    file = await bot.get_file(message.photo[-1].file_id)
    img = await bot.download_file(file.file_path)

    output = upscale_image(img.read())

    await message.answer_photo(
        photo=output,
        caption="✨ HD Enhanced!"
    )
