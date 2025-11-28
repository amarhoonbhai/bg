from aiogram import Router, types, F
from utils.check_member import check_all_membership
from utils.database import increment_stat
from services.face_fix import restore_face
from utils.buttons import verify_buttons

router = Router()

@router.message(F.photo)
async def face_fix_handler(message: types.Message, bot):
    if getattr(bot, "user_action", None) != "clean_face":
        return

    user_id = message.from_user.id
    ok = await check_all_membership(bot, user_id)

    if not ok:
        return await message.answer("🔐 Join all channels.", reply_markup=verify_buttons())

    file = await bot.get_file(message.photo[-1].file.file_id)
    img_bytes = await bot.download_file(file.file_path)

    output = restore_face(img_bytes.read())
    increment_stat("face")

    await message.answer_photo(output, caption="🧹 Face cleaned!")
