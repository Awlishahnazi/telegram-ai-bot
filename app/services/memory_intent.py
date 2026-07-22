class MemoryIntent:

    STORE = "store"
    UPDATE = "update"
    DELETE = "delete"
    CLEAR = "clear"
    NONE = "none"


    DELETE_PATTERNS = [
        "فراموش کن",
        "پاک کن",
        "حذف کن",
        "یادت نماند",
    ]


    CLEAR_PATTERNS = [
        "همه چیز را فراموش کن",
        "همه را پاک کن",
        "پاکسازی حافظه",
        "clear memory",
    ]


    UPDATE_PATTERNS = [
        "دیگر",
        "عوض شد",
        "تغییر کرد",
        "از این به بعد",
    ]


    def detect(
        self,
        message: str,
    ) -> str:

        text = message.lower()


        if any(
            pattern in text
            for pattern in self.CLEAR_PATTERNS
        ):
            return self.CLEAR


        if any(
            pattern in text
            for pattern in self.DELETE_PATTERNS
        ):
            return self.DELETE


        if any(
            pattern in text
            for pattern in self.UPDATE_PATTERNS
        ):
            return self.UPDATE


        return self.STORE


memory_intent = MemoryIntent()