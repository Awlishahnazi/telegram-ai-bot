from app.services.fact_extractor import fact_extractor
from app.repositories.user_fact_repository import user_fact_repository


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

        return user_fact_repository.get_context(user_id)


memory_manager = MemoryManager()