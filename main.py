import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, menu, remove_bg, cutout, stats, broadcast

async def main():
    bot = Bot(BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    bot.user_mode = None

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(remove_bg.router)
    dp.include_router(cutout.router)
    dp.include_router(stats.router)
    dp.include_router(broadcast.router)

    print("🔥 Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
