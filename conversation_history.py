class ConversationHistory:
    def __init__(self):
        self.messages = []

    def get(self):
        return self.messages
    
    def add(self, message):
        self.messages.append(message)
