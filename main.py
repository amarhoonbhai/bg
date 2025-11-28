import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import (
    start, verify, menu,
    remove_bg, enhance,
    dp_crop, face_restore,
    broadcast
)

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(verify.router)
    dp.include_router(menu.router)
    dp.include_router(remove_bg.router)
    dp.include_router(enhance.router)
    dp.include_router(dp_crop.router)
    dp.include_router(face_restore.router)
    dp.include_router(broadcast.router)

    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
