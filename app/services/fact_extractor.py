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
You are a memory extraction system.

Your task is to extract ONLY long-term facts about the user.

Allowed keys (ONLY use these keys):

- name
- nickname
- age
- birthday
- gender
- city
- country
- university
- major
- degree
- occupation
- company
- favorite_language
- favorite_framework
- hobby
- interest
- goal
- pet
- spoken_language

If a fact does not fit one of these keys, ignore it.

If the message contains no long-term facts, return exactly:

{{"facts": []}}

Return ONLY valid JSON.

Never include explanations.
Never include markdown.
Never include code fences.
Never invent facts.

Extract facts even when the user expresses preferences or interests.

Examples:

User:
من به یادگیری پایتون علاقه دارم

Output:

{{
 "facts":[
   {{
     "key":"favorite_language",
     "value":"Python"
   }}
 ]
}}


User:
من به هوش مصنوعی علاقه دارم

Output:

{{
 "facts":[
   {{
     "key":"interest",
     "value":"Artificial Intelligence"
   }}
 ]
}}


Format:

{{
    "facts": [
        {{
            "key": "...",
            "value": "..."
        }}
    ]
}}

For values:

- Keep names complete.
- Keep university names complete.
- Keep company names complete.
- Keep city names complete.
- Do not shorten values.
- Preserve the user's language whenever possible.

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

            print("MODEL OUTPUT:")
            print(text)

            return json.loads(text)

        except Exception:

            logger.exception("Fact extraction failed")

            return {"facts": []}


fact_extractor = FactExtractor()