from sqlalchemy import select

from app.database.database import SessionLocal
from app.database.models import UserFact


SINGLE_VALUE_KEYS = {
    "name",
    "nickname",
    "age",
    "birthday",
    "gender",
    "city",
    "country",
    "university",
    "major",
    "degree",
    "occupation",
    "company",
}


MULTI_VALUE_KEYS = {
    "interest",
    "hobby",
    "favorite_language",
    "favorite_framework",
    "goal",
    "pet",
    "spoken_language",
}


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

                # برای اطلاعات چند مقداری
                if key in MULTI_VALUE_KEYS:

                    existing_values = [
                        item.strip()
                        for item in fact.value.split(",")
                    ]

                    if value not in existing_values:
                        existing_values.append(value)

                        fact.value = ", ".join(existing_values)

                # برای اطلاعات تک مقداری
                else:
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
                .where(
                    UserFact.user_id == user_id
                )
            )

            facts = session.execute(stmt).scalars().all()

            return {
                fact.key: fact.value
                for fact in facts
            }

    def delete_fact(
        self,
        user_id: int,
        key: str,
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

            if fact is None:
                return False

            session.delete(fact)
            session.commit()

            return True

    def clear_all(
        self,
        user_id: int,
    ):

        with SessionLocal() as session:

            stmt = (
                select(UserFact)
                .where(
                    UserFact.user_id == user_id,
                )
            )

            facts = session.execute(stmt).scalars().all()

            for fact in facts:
                session.delete(fact)

            session.commit()

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