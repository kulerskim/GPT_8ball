from unittest.mock import MagicMock
from gpt_8ball import GPT8Ball

def test_call_chat_completion_creates_valid_api_call():
    gpt_8ball = GPT8Ball("")

    openai_mock = MagicMock()
    gpt_8ball.openai = openai_mock

    gpt_8ball.call_chat_completion("hello")
    
    openai_mock.ChatCompletion.create.assert_any_call(
        model=gpt_8ball.model, messages=[{"role": "user", "content": "hello"}]
    )
