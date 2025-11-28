from aiogram import Router, types
from utils.check_member import check_all_membership
from utils.database import increment_stat
from services.background import remove_background
from utils.buttons import verify_buttons

router = Router()


@router.message(lambda m: m.photo)
async def remove_bg_handler(message: types.Message, bot):
    action = getattr(bot, "user_action", None)
    if action != "remove_bg":
        return

    user_id = message.from_user.id
    ok = await check_all_membership(bot, user_id)
    if not ok:
        return await message.answer("🔐 Please join channels.", reply_markup=verify_buttons())

    file = await bot.get_file(message.photo[-1].file_id)
    img_bytes = await bot.download_file(file.file_path)

    output = remove_background(img_bytes.read())
    increment_stat("bg")

    await message.answer_photo(output, caption="🧼 <b>Background Removed!</b>")
