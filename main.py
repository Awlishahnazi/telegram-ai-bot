import asyncio

from app.bot import create_bot, dp
from app.handlers.start import router
from app.utils.logger import setup_logger


logger = setup_logger()


async def main():
    bot = await create_bot()

    dp.include_router(router)

    logger.info("Bot is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())