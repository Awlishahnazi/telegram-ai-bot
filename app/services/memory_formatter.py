class MemoryFormatter:

    LABELS = {
        "name": "👤 Name",
        "major": "🎓 Major",
        "university": "🏫 University",
        "goal": "🎯 Goal",
        "interest": "⭐ Interest",
        "favorite_language": "💻 Favorite Language",
        "occupation": "💼 Occupation",
        "city": "🏙 City",
    }


    def format(
        self,
        facts: dict,
    ) -> str:

        if not facts:
            return "🧠 No memory stored yet."

        text = "🧠 <b>Your Memory</b>\n\n"


        for key, value in facts.items():

            label = self.LABELS.get(
                key,
                key
            )

            text += (
                f"{label}: "
                f"{value}\n\n"
            )


        return text.strip()



memory_formatter = MemoryFormatter()