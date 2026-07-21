from app.repositories.user_fact_repository import user_fact_repository


class ProfileService:

    def get_profile(
        self,
        user_id: int,
    ):

        facts = user_fact_repository.get_facts(user_id)

        if not facts:
            return None

        text = "👤 Your Profile\n\n"

        mapping = {
            "name": "👤 Name",
            "major": "🎓 Major",
            "university": "🏫 University",
            "favorite_language": "💻 Favorite Language",
            "interest": "⭐ Interest",
            "goal": "🎯 Goal",
            "occupation": "💼 Occupation",
            "city": "🏙 City",
        }

        for key, value in facts.items():

            label = mapping.get(
                key,
                key
            )

            text += f"{label}: {value}\n"

        return text


profile_service = ProfileService()