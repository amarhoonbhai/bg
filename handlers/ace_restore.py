from aiogram import Router, types
from utils.check_member import check_all_membership
from services.face_fix import restore_face

router = Router()


@router.message(lambda m: m.photo)
async def face_fix_handler(message: types.Message, bot):
    action = getattr(bot, "user_action", None)
    if action != "clean_face":
        return

    user_id = message.from_user.id
    ok = await check_all_membership(bot, user_id)
    if not ok:
        from utils.buttons import verify_buttons
        return await message.answer("🔐 Please join channels.", reply_markup=verify_buttons())

    file = await bot.get_file(message.photo[-1].file_id)
    img = await bot.download_file(file.file_path)

    output = restore_face(img.read())

    await message.answer_photo(
        photo=output,
        caption="🧹 Face Cleaned!"
    )
