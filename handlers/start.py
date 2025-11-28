from aiogram import Router, types
from aiogram.filters import Command
from utils.database import add_user
from utils.check_member import check_all_membership
from utils.buttons import main_menu, verify_button
from datetime import datetime
import pytz

router = Router()

def time_greet():
    ist = pytz.timezone("Asia/Kolkata")
    hour = datetime.now(ist).hour

    if 4 <= hour < 11:
        return "🌅 Good Morning"
    elif 11 <= hour < 17:
        return "🌤 Good Afternoon"
    elif 17 <= hour < 21:
        return "🌆 Good Evening"
    else:
        return "🌌 Good Night"


@router.message(Command("start"))
async def start_cmd(message: types.Message, bot):
    user = message.from_user
    first = user.first_name or ""
    last = user.last_name or ""

    name = first + (" " + last if last else "")
    add_user(user.id)

    ok = await check_all_membership(bot, user.id)
    if not ok:
        return await message.answer(
            "🔐 <b>Please join all required channels to continue.</b>",
            reply_markup=verify_button()
        )

    # Fetch profile picture
    dp = None
    try:
        photos = await bot.get_user_profile_photos(user.id)
        if photos.total_count > 0:
            dp = photos.photos[0][0].file_id
    except:
        pass

    greet = time_greet()

    welcome_msg = f"""
{greet}, <b>{name}</b>! 👋

✨ Welcome to <b>Instant BG Remover Bot</b>

🧼 Remove Background  
✂️ Smart Cut-Out  
⏱ Fast, Clean & Professional  

Choose a tool below to get started.
"""

    if dp:
        await message.answer_photo(dp, caption=welcome_msg, reply_markup=main_menu())
    else:
        await message.answer(welcome_msg, reply_markup=main_menu())
