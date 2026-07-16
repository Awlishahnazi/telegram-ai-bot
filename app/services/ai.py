import logging
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.memory import memory_service
from openai import AsyncOpenAI

from app.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)


logger = logging.getLogger("telegram-ai-bot")



class AIService:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL,
        )

    async def generate_response(self, user_id: int, message: str ) -> str:
        """
        Generate AI response using OpenRouter.
        """

        logger.info(
            "Generating AI response for message: %s",
            message
        )

        try:
            memory_service.add_user_message(user_id, message)
            history = memory_service.get_history(user_id)

            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },

                    *history,
                ],
            )

            reply = response.choices[0].message.content
            memory_service.add_assistant_message(user_id, reply)
            return reply

        except Exception:
            logger.exception(
                "AI generation failed"
            )

            return (
                "متاسفانه در ارتباط با سرویس AI مشکلی پیش آمد."
            )


ai_service = AIService()