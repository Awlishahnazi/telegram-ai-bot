import logging
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.memory import memory_service
from openai import AsyncOpenAI
from app.services.memory_manager import memory_manager
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

    async def generate_response(self, user_id: int, message: str) -> str:
        """
        Generate AI response using OpenRouter.
        """

        logger.info(
            "Generating AI response for message: %s",
            message
        )

        try:
            memory_service.add_user_message(user_id, message)

            await memory_manager.process_message(user_id, message)
            
            history = memory_service.get_history(user_id)

            user_context = memory_manager.get_user_context(user_id)
            system_content = SYSTEM_PROMPT
            if user_context:
                system_content += f"""

            Known information about the user:

            {user_context}

            Use this information when it is relevant.
            Do not mention that you have memory unless the user asks.

            """

            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
                messages=[
                    {
                        "role": "system",
                        "content": system_content,
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