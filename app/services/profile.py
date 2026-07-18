from app.repositories.user_fact_repository import user_fact_repository


class ProfileService:

    def build_profile(
        self,
        user_id: int,
    ) -> str:

        facts = user_fact_repository.get_facts(user_id)

        if not facts:
            return (
                "🧠 هنوز اطلاعاتی درباره شما ذخیره نشده است."
            )

        lines = [
            "🧠 Your Memory",
            "",
        ]

        labels = {
            "name": "👤 Name",
            "nickname": "😊 Nickname",
            "age": "🎂 Age",
            "city": "🏙 City",
            "country": "🌍 Country",
            "major": "🎓 Major",
            "university": "🏫 University",
            "occupation": "💼 Occupation",
            "company": "🏢 Company",
            "favorite_language": "💻 Favorite Language",
            "favorite_framework": "⚙️ Favorite Framework",
            "interest": "❤️ Interest",
            "hobby": "🎯 Hobby",
            "goal": "🚀 Goal",
            "pet": "🐶 Pet",
            "spoken_language": "🗣 Language",
        }

        for key, value in facts.items():

            label = labels.get(key, key)

            lines.append(
                f"{label}: {value}"
            )

        return "\n".join(lines)


profile_service = ProfileService()