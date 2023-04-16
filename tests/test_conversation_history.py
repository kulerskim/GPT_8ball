from conversation_history import ConversationHistory

def test_conversation_history_get():
    conversation_history = ConversationHistory()
    messages = conversation_history.get()
    assert messages == []

def test_conversation_history_add():
    test_message = "test message"
    conversation_history = ConversationHistory()
    conversation_history.add(test_message)
    assert conversation_history.messages[-1] == test_message