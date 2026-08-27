class VoiceSystem:
    def __init__(self):
        self.listening = False

    def start_listening(self):
        self.listening = True
        return "Listening..."

    def stop_listening(self):
        self.listening = False
        return "Listening stopped."


voice = VoiceSystem()
