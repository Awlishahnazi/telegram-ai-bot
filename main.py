import asyncio

from app.bot import create_bot, dp
from app.handlers.start import router


async def main():
    bot = await create_bot()

    dp.include_router(router)

    print("✅ Bot is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())