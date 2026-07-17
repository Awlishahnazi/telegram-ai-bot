from app.database.database import SessionLocal
from app.database.models import Message


MAX_HISTORY = 10


class MemoryService:

    def add_user_message(
        self,
        user_id: int,
        content: str
    ):
        self._save(
            user_id,
            "user",
            content
        )


    def add_assistant_message(
        self,
        user_id: int,
        content: str
    ):
        self._save(
            user_id,
            "assistant",
            content
        )


    def get_history(
        self,
        user_id: int
    ):
        with SessionLocal() as session:

            messages = (
                session.query(Message)
                .filter(
                    Message.user_id == user_id
                )
                .order_by(
                    Message.created_at.asc()
                )
                .all()
            )

            messages = messages[-MAX_HISTORY:]

            return [
                {
                    "role": message.role,
                    "content": message.content,
                }
                for message in messages
            ]


    def clear(
        self,
        user_id: int
    ):
        with SessionLocal() as session:

            session.query(Message).filter(
                Message.user_id == user_id
            ).delete()

            session.commit()


    def _save(
        self,
        user_id: int,
        role: str,
        content: str
    ):

        with SessionLocal() as session:

            message = Message(
                user_id=user_id,
                role=role,
                content=content,
            )

            session.add(message)
            session.commit()



memory_service = MemoryService()