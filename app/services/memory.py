from collections import defaultdict

MAX_HISTORY = 10


class MemoryService:
    def __init__(self):
        self.memory = defaultdict(list)

    def get_history(self, user_id: int):
        return self.memory[user_id]

    def add_user_message(self, user_id: int, content: str):
        self.memory[user_id].append(
            {
                "role": "user",
                "content": content,
            }
        )
        self._trim(user_id)

    def add_assistant_message(self, user_id: int, content: str):
        self.memory[user_id].append(
            {
                "role": "assistant",
                "content": content,
            }
        )
        self._trim(user_id)

    def clear(self, user_id: int):
        self.memory[user_id].clear()

    def _trim(self, user_id: int):
        if len(self.memory[user_id]) > MAX_HISTORY:
            self.memory[user_id] = self.memory[user_id][-MAX_HISTORY:]


memory_service = MemoryService()