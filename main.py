import asyncio
import logging

from app.bot import create_bot, dp
from app.handlers.start import router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("telegram-ai-bot")


async def main():
    bot = await create_bot()

    dp.include_router(router)

    logger.info("Bot is running...")

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()
        logger.info("Bot stopped gracefully.")


if __name__ == "__main__":
    asyncio.run(main())