class MemoryStore:
    def __init__(self):
        self.memories = []

    def add(self, memory: str):
        self.memories.append(memory)
        return "Memory stored."

    def get_all(self):
        return self.memories

    def clear(self):
        self.memories.clear()
        return "Memory cleared."


memory = MemoryStore()
