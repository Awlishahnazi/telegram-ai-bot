from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.services.ai import ai_service


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "سلام 👋\n\n"
        "من ربات هوش مصنوعی تو هستم.\n"
        "پیامت را بفرست تا با هم صحبت کنیم 🤖"
    )


@router.message()
async def chat_handler(message: Message):
    if not message.text:
        await message.answer(
            "فعلاً فقط پیام متنی را پردازش می‌کنم 🤖"
        )
        return

    response = await ai_service.generate_response(
    user_id=message.from_user.id,
    message=message.text,
    )

    await message.answer(response)