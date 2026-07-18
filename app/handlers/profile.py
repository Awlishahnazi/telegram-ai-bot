from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.profile import profile_service

router = Router()


@router.message(Command("memory"))
async def memory_command(message: Message):

    profile = profile_service.build_profile(
        message.from_user.id,
    )

    await message.answer(profile)