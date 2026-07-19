from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.memory_manager import memory_manager


router = Router()


@router.message(Command("debug_memory"))
async def debug_memory_command(message: Message):

    user_id = message.from_user.id

    context = memory_manager.debug_context(
        user_id=user_id
    )

    await message.answer(
        context
    )