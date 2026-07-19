from app.repositories.user_fact_repository import user_fact_repository
from app.services.fact_extractor import fact_extractor
from app.services.memory_ranker import memory_ranker


class MemoryManager:

    async def process_message(
        self,
        user_id: int,
        message: str,
    ):

        result = await fact_extractor.extract(message)

        facts = result.get("facts", [])

        for fact in facts:

            user_fact_repository.save_fact(
                user_id=user_id,
                key=fact["key"],
                value=fact["value"],
            )

    def get_user_context(
        self,
        user_id: int,
    ):

        facts = user_fact_repository.get_facts(user_id)

        if not facts:
            return ""

        ranked_facts = memory_ranker.rank(facts)

        return "\n".join(
            f"{key}: {value}"
            for key, value in ranked_facts.items()
        )

    def debug_context(
        self,
        user_id: int,
    ):

        facts = user_fact_repository.get_facts(user_id)

        if not facts:
            return "No memory."

        ranked = memory_ranker.rank(facts)

        text = "🧠 Memory Context\n\n"

        for key, value in ranked.items():

            score = memory_ranker.score(key)

            text += (
                f"{score:>3} | "
                f"{key}: "
                f"{value}\n"
            )

        return text


memory_manager = MemoryManager()