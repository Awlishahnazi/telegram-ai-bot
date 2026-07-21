from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.repositories.user_fact_repository import user_fact_repository
from app.services.memory_formatter import memory_formatter


router = Router()


@router.message(Command("memory"))
async def show_memory(message: Message):

    user_id = message.from_user.id

    facts = user_fact_repository.get_facts(user_id)

    if not facts:
        await message.answer(
            "🧠 هنوز اطلاعاتی از شما ذخیره نشده است."
        )
        return


    text = memory_formatter.format(
        facts
    )


    await message.answer(
        text,
        parse_mode="HTML"
    )