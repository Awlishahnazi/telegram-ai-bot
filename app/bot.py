from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from app.config import BOT_TOKEN


async def create_bot():
    session = AiohttpSession()

    bot = Bot(
        token=BOT_TOKEN,
        session=session
    )

    return bot


dp = Dispatcher()