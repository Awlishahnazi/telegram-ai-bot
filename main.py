import asyncio
import logging
from app.bot import create_bot, dp
from app.handlers.start import router as start_router
from app.handlers.memory import router as memory_router
from app.handlers.profile import router as profile_router
from app.handlers.menu import router as menu_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("telegram-ai-bot")


async def main():
    bot = await create_bot()

    dp.include_router(menu_router)
    dp.include_router(profile_router)
    dp.include_router(memory_router)
    dp.include_router(start_router)

    logger.info("Bot is running...")

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()
        logger.info("Bot stopped gracefully.")


if __name__ == "__main__":
    asyncio.run(main())