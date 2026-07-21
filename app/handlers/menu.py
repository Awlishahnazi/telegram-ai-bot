from aiogram import Router
from aiogram.types import Message
from app.repositories.user_fact_repository import user_fact_repository
from app.services.profile import profile_service
from app.services.memory_formatter import memory_formatter


router = Router()





@router.message(lambda message: message.text == "🧠 My Memory")
async def memory_button_handler(message: Message):

    user_id = message.from_user.id

    facts = user_fact_repository.get_facts(
        user_id
    )

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


@router.message(lambda message: message.text == "👤 My Profile")
async def profile_button_handler(message: Message):

    profile = profile_service.get_profile(
        message.from_user.id
    )

    if not profile:
        await message.answer(
            "👤 هنوز اطلاعاتی از شما ذخیره نشده است."
        )
        return

    await message.answer(profile)


@router.message(lambda message: message.text == "⚙️ Settings")
async def settings_button_handler(message: Message):

    await message.answer(
        "⚙️ Settings\n\n"
        "این بخش در نسخه‌های بعدی اضافه خواهد شد."
    )


@router.message(lambda message: message.text == "💬 Chat with AI")
async def chat_button_handler(message: Message):

    await message.answer(
        "💬 آماده گفتگو هستم. پیام خود را ارسال کنید."
    )