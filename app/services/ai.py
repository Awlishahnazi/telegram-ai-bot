import logging
from app.prompts.system_prompt import SYSTEM_PROMPT
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

    async def generate_response(self, message: str) -> str:
        """
        Generate AI response using OpenRouter.
        """

        logger.info(
            "Generating AI response for message: %s",
            message
        )

        try:
            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": message,
                    },
                ],
            )

            return response.choices[0].message.content

        except Exception:
            logger.exception(
                "AI generation failed"
            )

            return (
                "متاسفانه در ارتباط با سرویس AI مشکلی پیش آمد."
            )


ai_service = AIService()