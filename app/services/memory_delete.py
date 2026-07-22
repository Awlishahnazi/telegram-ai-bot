from app.repositories.user_fact_repository import user_fact_repository


class MemoryDelete:

    KEYWORDS = {

        "name": [
            "اسم",
            "نام",
        ],

        "city": [
            "شهر",
            "محل زندگی",
        ],

        "major": [
            "رشته",
        ],

        "university": [
            "دانشگاه",
        ],

        "goal": [
            "هدف",
        ],

        "interest": [
            "علاقه",
        ],

        "favorite_language": [
            "پایتون",
            "زبان برنامه نویسی",
            "زبان",
        ],

        "occupation": [
            "شغل",
            "کار",
        ],
    }


    def delete(
        self,
        user_id: int,
        message: str,
    ) -> list:

        text = message.lower()

        deleted = []

        facts = user_fact_repository.get_facts(user_id)


        for key, keywords in self.KEYWORDS.items():

            if key not in facts:
                continue


            if any(
                keyword.lower() in text
                for keyword in keywords
            ):

                user_fact_repository.delete_fact(
                    user_id=user_id,
                    key=key,
                )

                deleted.append(key)


        return deleted



memory_delete = MemoryDelete()