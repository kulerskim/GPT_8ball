from unittest.mock import MagicMock
from gpt_8ball import GPT8Ball

def test_call_chat_completion_creates_valid_api_call():
    gpt_8ball = GPT8Ball()

    openai_mock = MagicMock()
    gpt_8ball.openai = openai_mock

    gpt_8ball.call_chat_completion("hello")
    
    openai_mock.ChatCompletion.create.called_with(
        model=gpt_8ball.model, messages=[{"role": "user", "content": "hello"}]
    )

def test_call_chat_completion_keeps_conversation_history():
    gpt_8ball = GPT8Ball()

    openai_mock = MagicMock()
    openai_mock.ChatCompletion.create.return_value = {
        "choices": [{
            "message": {
                "role": "assistant",
                "content": "Hi there, I'm your assistant how can I help you?"
            }
        }]
    }

    gpt_8ball.openai = openai_mock

    gpt_8ball.call_chat_completion("hello")
    gpt_8ball.call_chat_completion("bye bye")

    openai_mock.ChatCompletion.create.assert_called_with(
        model=gpt_8ball.model, messages=[
            {"role": "user", "content": "hello"},
            {"role": "assistant", "content": "Hi there, I'm your assistant how can I help you?"},
            {"role": "user", "content": "bye bye"}
        ]
    )


