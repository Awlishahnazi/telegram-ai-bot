import logging

from aiogram import Router
from aiogram.types import ErrorEvent

router = Router()

logger = logging.getLogger("telegram-ai-bot")


@router.error()
async def error_handler(event: ErrorEvent):
    logger.exception(
        "Exception occurred while processing update",
        exc_info=event.exception
    )

    return True