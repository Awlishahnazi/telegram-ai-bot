class MemorySearch:

    KEYWORDS = {
        "goal": [
            "هدف",
            "آینده",
            "career",
            "job",
            "اپلای",
            "goal",
        ],
        "interest": [
            "علاقه",
            "دوست دارم",
            "عاشق",
            "هوش مصنوعی",
            "AI",
            "machine learning",
        ],
        "favorite_language": [
            "پایتون",
            "python",
            "جاوا",
            "java",
            "زبان برنامه نویسی",
            "language",
        ],
        "major": [
            "دانشگاه",
            "رشته",
            "مهندسی",
            "درس",
            "دانشجو",
        ],
        "university": [
            "دانشگاه",
            "campus",
        ],
        "name": [
            "اسم",
            "نام",
            "کی هستم",
        ],
        "city": [
            "شهر",
            "محل زندگی",
        ],
        "occupation": [
            "شغل",
            "کار",
            "job",
        ],
    }

    def search(
        self,
        message: str,
        facts: dict,
    ):

        message = message.lower()

        result = {}

        for key, keywords in self.KEYWORDS.items():

            if key not in facts:
                continue

            if any(
                keyword.lower() in message
                for keyword in keywords
            ):
                result[key] = facts[key]

        return result


memory_search = MemorySearch()