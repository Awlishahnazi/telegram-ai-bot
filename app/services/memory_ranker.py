FACT_SCORES = {
    "name": 100,
    "goal": 95,
    "major": 90,
    "university": 90,
    "degree": 85,
    "occupation": 85,
    "company": 80,
    "city": 75,
    "country": 75,
    "favorite_language": 70,
    "favorite_framework": 65,
    "spoken_language": 60,
    "interest": 50,
    "hobby": 40,
    "pet": 20,
}


class MemoryRanker:

    def score(
        self,
        key: str,
    ) -> int:

        return FACT_SCORES.get(key, 0)

    def rank(
        self,
        facts: dict,
        limit: int = 10,
    ):

        ranked = sorted(
            facts.items(),
            key=lambda item: self.score(item[0]),
            reverse=True,
        )

        return dict(ranked[:limit])


memory_ranker = MemoryRanker()