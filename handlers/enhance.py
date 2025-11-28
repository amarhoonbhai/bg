from aiogram import Router, types, F
from utils.check_member import check_all_membership
from utils.database import increment_stat
from services.enhance import upscale_image
from utils.buttons import verify_buttons

router = Router()   # <-- REQUIRED (this is missing in your file)

@router.message(F.photo)
async def enhance_handler(message: types.Message, bot):
    # Check if user selected Enhance option
    if getattr(bot, "user_action", None) != "enhance_hd":
        return

    user_id = message.from_user.id

    # Membership check
    ok = await check_all_membership(bot, user_id)
    if not ok:
        return await message.answer(
            "🔐 Join all required channels first.",
            reply_markup=verify_buttons()
        )

    # Download file
    file = await bot.get_file(message.photo[-1].file_id)
    img_bytes = await bot.download_file(file.file_path)

    # Enhance using LITE upscaler
    output = upscale_image(img_bytes.read())

    # Update stats
    increment_stat("enhance")

    # Send result
    await message.answer_photo(
        output,
        caption="✨ HD Enhanced!"
    )
