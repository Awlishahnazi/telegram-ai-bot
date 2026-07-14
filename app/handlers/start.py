from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "سلام 👋\n\n"
        "من ربات هوش مصنوعی تو هستم.\n"
        "به‌زودی می‌توانی با من گفتگو کنی. 🤖"
    )