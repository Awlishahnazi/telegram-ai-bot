import logging

from openai import AsyncOpenAI

from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.memory import memory_service
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


    async def generate_response(
        self,
        user_id: int,
        message: str
    ) -> str:
        """
        Generate AI response using OpenRouter
        with long-term user memory.
        """

        logger.info(
            "Generating AI response for message: %s",
            message
        )


        try:

            # Save user's message in short-term memory
            memory_service.add_user_message(
                user_id,
                message
            )


            # Extract and save long-term facts
            await memory_manager.process_message(
                user_id,
                message
            )


            # Get conversation history
            history = memory_service.get_history(
                user_id
            )


            # Get long-term memory context
            user_context = memory_manager.get_user_context(
            user_id=user_id,
            message=message,
            )


            system_content = SYSTEM_PROMPT


            if user_context:

                system_content += f"""

Known information about the user:

{user_context}


Instructions:

- Use this information only when relevant.
- Do not mention memory system.
- Do not say "I remember from memory".
- Answer naturally based on conversation context.

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


            # Save AI response
            memory_service.add_assistant_message(
                user_id,
                reply
            )


            return reply



        except Exception:

            logger.exception(
                "AI generation failed"
            )

            return (
                "متاسفانه در ارتباط با سرویس AI مشکلی پیش آمد."
            )


ai_service = AIService()