class MemoryCleaner:

    def should_store(
        self,
        key: str,
        value: str,
        existing: dict,
    ):

        old = existing.get(key)

        if old is None:
            return True

        if old == value:
            return False

        return True


memory_cleaner = MemoryCleaner()