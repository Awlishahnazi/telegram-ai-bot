import logging

logger = logging.getLogger("telegram-ai-bot")


class AIService:

    async def generate_response(self, message: str) -> str:
        """
        Generate AI response.
        This will be connected to OpenRouter later.
        """

        logger.info(
            "Generating AI response for message: %s",
            message
        )

        return f"You said: {message}"


ai_service = AIService()