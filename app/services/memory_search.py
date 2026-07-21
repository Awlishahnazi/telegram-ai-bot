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
            "زبان",
            "language",
            "مورد علاقه",
            "علاقه",
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
            "من کی هستم",
            "من چیست",
        ],
        "city": [
            "شهر",
            "محل زندگی",
            "زندگی می‌کنم",
        "کجا",
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