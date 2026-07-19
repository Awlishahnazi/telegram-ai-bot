from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from app.services.ai import ai_service
from app.keyboards.main_menu import get_main_menu


router = Router()


MENU_BUTTONS = [
    "💬 Chat with AI",
    "🧠 My Memory",
    "👤 My Profile",
    "⚙️ Settings",
]


@router.message(Command("start"))
async def start_handler(message: Message):

    await message.answer(
        "🤖 سلام!\n\n"
        "من Alish AI هستم.\n"
        "می‌توانم با شما گفتگو کنم و اطلاعات مهم شما را به خاطر بسپارم.",
        reply_markup=get_main_menu()
    )


@router.message(
    F.text,
    ~F.text.in_(MENU_BUTTONS),
    ~F.text.startswith("/")
)
async def chat_handler(message: Message):

    response = await ai_service.generate_response(
        user_id=message.from_user.id,
        message=message.text
    )

    await message.answer(response)