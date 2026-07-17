from sqlalchemy import select

from app.database.database import SessionLocal
from app.database.models import Message


class MessageRepository:

    def add_message(
        self,
        user_id: int,
        role: str,
        content: str,
    ):
        with SessionLocal() as session:

            message = Message(
                user_id=user_id,
                role=role,
                content=content,
            )

            session.add(message)
            session.commit()

    def get_history(
        self,
        user_id: int,
        limit: int = 10,
    ):

        with SessionLocal() as session:

            stmt = (
                select(Message)
                .where(Message.user_id == user_id)
                .order_by(Message.id.desc())
                .limit(limit)
            )

            messages = session.execute(stmt).scalars().all()

            messages.reverse()

            return [
                {
                    "role": m.role,
                    "content": m.content,
                }
                for m in messages
            ]


message_repository = MessageRepository()