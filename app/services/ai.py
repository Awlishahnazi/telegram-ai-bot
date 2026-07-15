import logging

from openai import AsyncOpenAI

from app.config import OPENROUTER_API_KEY


logger = logging.getLogger("telegram-ai-bot")


client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


class AIService:

    async def generate_response(self, message: str) -> str:
        """
        Generate AI response using OpenRouter.
        """

        logger.info(
            "Generating AI response for message: %s",
            message
        )

        try:
            response = await client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.exception(
                "AI generation failed"
            )

            return (
                "متاسفانه در ارتباط با سرویس AI مشکلی پیش آمد."
            )


ai_service = AIService()