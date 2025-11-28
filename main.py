import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from handlers import start, menu, remove_bg, cutout, stats, broadcast


async def main():
    # Init bot
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # global var for mode
    bot.user_mode = None

    # include routers
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(remove_bg.router)
    dp.include_router(cutout.router)
    dp.include_router(stats.router)
    dp.include_router(broadcast.router)

    print("🔥 BOT STARTED SUCCESSFULLY — READY TO USE")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
