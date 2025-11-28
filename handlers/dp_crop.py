from aiogram import Router, types, F
from utils.check_member import check_all_membership
from utils.database import increment_stat
from services.dp_crop import auto_crop_dp
from utils.buttons import verify_buttons

router = Router()

@router.message(F.photo)
async def dp_crop_handler(message: types.Message, bot):
    if getattr(bot, "user_action", None) != "dp_crop":
        return

    user_id = message.from_user.id
    ok = await check_all_membership(bot, user_id)

    if not ok:
        return await message.answer("🔐 Join channels first.", reply_markup=verify_buttons())

    file = await bot.get_file(message.photo[-1].file_id)
    img_bytes = await bot.download_file(file.file_path)

    output = auto_crop_dp(img_bytes.read())
    increment_stat("dp")

    await message.answer_photo(output, caption="📸 DP cropped!")
