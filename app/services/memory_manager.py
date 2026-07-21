from app.repositories.user_fact_repository import user_fact_repository
from app.services.fact_extractor import fact_extractor
from app.services.memory_ranker import memory_ranker
from app.services.memory_cleaner import memory_cleaner
from app.services.memory_search import memory_search


class MemoryManager:

    async def process_message(
        self,
        user_id: int,
        message: str,
    ):

        result = await fact_extractor.extract(message)

        facts = result.get("facts", [])

        if not facts:
            return

        existing = user_fact_repository.get_facts(user_id)

        for fact in facts:

            key = fact["key"]
            value = fact["value"]

            if not memory_cleaner.should_store(
                key,
                value,
                existing,
            ):
                continue

            user_fact_repository.save_fact(
                user_id=user_id,
                key=key,
                value=value,
            )

            # Update local memory state
            # to handle multiple facts in one message
            existing[key] = value


    def search_memory(
        self,
        user_id: int,
        message: str,
    ):
        """
        Retrieve relevant memories based on user query.
        """

        facts = user_fact_repository.get_facts(user_id)

        if not facts:
            return ""

        relevant = memory_search.search(
            message,
            facts,
        )

        if not relevant:
            return ""

        ranked = memory_ranker.rank(relevant)

        return "\n".join(
            f"{key}: {value}"
            for key, value in ranked.items()
        )


    def get_user_context(
        self,
        user_id: int,
        message: str,
    ):
        """
        Generate context for AI prompt.
        """

        context = self.search_memory(
            user_id,
            message,
        )

        return context


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