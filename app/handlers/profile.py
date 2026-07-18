from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.profile import profile_service

router = Router()


@router.message(Command("profile"))
async def profile_command(message: Message):

    profile = profile_service.get_profile(
        message.from_user.id,
    )

    if profile is None:
        profile = (
            "👤 هنوز اطلاعاتی درباره شما ذخیره نشده است."
        )

    await message.answer(profile)