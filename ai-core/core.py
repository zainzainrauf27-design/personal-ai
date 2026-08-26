class AICore:
    def __init__(self):
        self.name = "Personal AI"

    def process(self, user_input: str) -> str:
        """
        Process a user command.

        The intelligence layer will be connected here later.
        """
        return f"Received: {user_input}"


ai = AICore()
