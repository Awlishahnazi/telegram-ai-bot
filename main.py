import asyncio
from app.bot import create_bot, dp
from app.handlers.start import router
from app.handlers.errors import router as error_router
from app.utils.logger import setup_logger


logger = setup_logger()

async def main():
    bot = await create_bot()

    dp.include_router(router)
    dp.include_router(error_router)

    logger.info("Bot is running...")

    try:
        await dp.start_polling(bot)

    finally:
        logger.info("Bot stopped")
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())