from sqlalchemy import select

from app.database.database import SessionLocal
from app.database.models import UserFact


class UserFactRepository:

    def save_fact(
        self,
        user_id: int,
        key: str,
        value: str,
    ):
        with SessionLocal() as session:

            stmt = (
                select(UserFact)
                .where(
                    UserFact.user_id == user_id,
                    UserFact.key == key,
                )
            )

            fact = session.execute(stmt).scalar_one_or_none()

            if fact:
                fact.value = value
            else:
                fact = UserFact(
                    user_id=user_id,
                    key=key,
                    value=value,
                )
                session.add(fact)

            session.commit()

    def get_facts(
        self,
        user_id: int,
    ):

        with SessionLocal() as session:

            stmt = (
                select(UserFact)
                .where(UserFact.user_id == user_id)
            )

            facts = session.execute(stmt).scalars().all()

            return {
                fact.key: fact.value
                for fact in facts
            }
        
    def get_context(
        self,
        user_id: int,
    ):

        facts = self.get_facts(user_id)

        if not facts:
            return ""

        return "\n".join(
            [
                f"{key}: {value}"
                for key, value in facts.items()
            ]
        )


user_fact_repository = UserFactRepository()