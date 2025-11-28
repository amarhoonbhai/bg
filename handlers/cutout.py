from aiogram import Router, types, F
from services.cutout import do_cutout
from utils.database import increment
from utils.check_member import check_all_membership

router = Router()

@router.message(F.photo)
async def cutout_handler(message: types.Message, bot):
    if getattr(bot, "user_mode", None) != "cutout":
        return

    if not await check_all_membership(bot, message.from_user.id):
        return await message.answer("❌ You must join required channels.")

    status = await message.answer("⏳ Cutting out object…")

    file = await bot.get_file(message.photo[-1].file_id)
    img = await bot.download_file(file.file_path)

    output = do_cutout(img.read())
    increment(message.from_user.id)

    await status.delete()
    await message.answer_photo(output, caption="✂️ Cut-Out Complete!")
