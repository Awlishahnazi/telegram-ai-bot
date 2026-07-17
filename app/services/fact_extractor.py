import json
import logging

from openai import AsyncOpenAI

from app.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    MODEL_NAME,
)

logger = logging.getLogger("telegram-ai-bot")


class FactExtractor:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL,
        )

    async def extract(self, message: str):

        prompt = f"""
Extract permanent user facts.

Return ONLY valid JSON.

Format:

{{
    "facts":[
        {{
            "key":"...",
            "value":"..."
        }}
    ]
}}

If there is no useful fact return

{{"facts":[]}}

Message:
{message}
"""

        try:

            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                temperature=0,
                max_tokens=200,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            text = response.choices[0].message.content

            return json.loads(text)

        except Exception:

            logger.exception("Fact extraction failed")

            return {"facts": []}


fact_extractor = FactExtractor()