from app.database.repository import message_repository


class MemoryService:

    def get_history(
        self,
        user_id: int,
    ):
        return message_repository.get_history(user_id)

    def add_user_message(
        self,
        user_id: int,
        content: str,
    ):
        message_repository.add_message(
            user_id=user_id,
            role="user",
            content=content,
        )

    def add_assistant_message(
        self,
        user_id: int,
        content: str,
    ):
        message_repository.add_message(
            user_id=user_id,
            role="assistant",
            content=content,
        )


memory_service = MemoryService()