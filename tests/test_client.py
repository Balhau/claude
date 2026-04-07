"""Tests for the ClaudeClient."""

import pytest
from unittest.mock import MagicMock, patch

from claude.client import ClaudeClient


@pytest.fixture
def mock_anthropic(monkeypatch):
    """Patch the anthropic.Anthropic constructor and return the mock instance."""
    mock_instance = MagicMock()
    mock_class = MagicMock(return_value=mock_instance)
    monkeypatch.setattr("claude.client.anthropic.Anthropic", mock_class)
    return mock_instance


class TestClaudeClientInit:
    def test_raises_without_api_key(self, monkeypatch):
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        with pytest.raises(ValueError, match="API key"):
            ClaudeClient()

    def test_accepts_api_key_argument(self, mock_anthropic):
        client = ClaudeClient(api_key="test-key")
        assert client.model == ClaudeClient.DEFAULT_MODEL

    def test_accepts_env_api_key(self, monkeypatch, mock_anthropic):
        monkeypatch.setenv("ANTHROPIC_API_KEY", "env-key")
        client = ClaudeClient()
        assert client.model == ClaudeClient.DEFAULT_MODEL

    def test_custom_model(self, mock_anthropic):
        client = ClaudeClient(api_key="test-key", model="claude-3-haiku-20240307")
        assert client.model == "claude-3-haiku-20240307"


class TestClaudeClientMessage:
    def test_message_returns_text(self, mock_anthropic):
        mock_content = MagicMock()
        mock_content.text = "Paris"
        mock_anthropic.messages.create.return_value = MagicMock(
            content=[mock_content]
        )

        client = ClaudeClient(api_key="test-key")
        result = client.message("What is the capital of France?")

        assert result == "Paris"

    def test_message_passes_system_prompt(self, mock_anthropic):
        mock_content = MagicMock()
        mock_content.text = "Sure!"
        mock_anthropic.messages.create.return_value = MagicMock(
            content=[mock_content]
        )

        client = ClaudeClient(api_key="test-key")
        client.message("Hello", system="You are a helpful assistant.")

        call_kwargs = mock_anthropic.messages.create.call_args.kwargs
        assert call_kwargs["system"] == "You are a helpful assistant."

    def test_message_no_system_prompt_by_default(self, mock_anthropic):
        mock_content = MagicMock()
        mock_content.text = "Hello!"
        mock_anthropic.messages.create.return_value = MagicMock(
            content=[mock_content]
        )

        client = ClaudeClient(api_key="test-key")
        client.message("Hello")

        call_kwargs = mock_anthropic.messages.create.call_args.kwargs
        assert "system" not in call_kwargs

    def test_message_custom_max_tokens(self, mock_anthropic):
        mock_content = MagicMock()
        mock_content.text = "Response"
        mock_anthropic.messages.create.return_value = MagicMock(
            content=[mock_content]
        )

        client = ClaudeClient(api_key="test-key")
        client.message("Hello", max_tokens=512)

        call_kwargs = mock_anthropic.messages.create.call_args.kwargs
        assert call_kwargs["max_tokens"] == 512


class TestClaudeClientStreamMessage:
    def test_stream_message_yields_chunks(self, mock_anthropic):
        mock_stream_ctx = MagicMock()
        mock_stream_ctx.__enter__ = MagicMock(return_value=mock_stream_ctx)
        mock_stream_ctx.__exit__ = MagicMock(return_value=False)
        mock_stream_ctx.text_stream = iter(["Hello", ", ", "world!"])
        mock_anthropic.messages.stream.return_value = mock_stream_ctx

        client = ClaudeClient(api_key="test-key")
        chunks = list(client.stream_message("Say hello"))

        assert chunks == ["Hello", ", ", "world!"]

    def test_stream_message_passes_system_prompt(self, mock_anthropic):
        mock_stream_ctx = MagicMock()
        mock_stream_ctx.__enter__ = MagicMock(return_value=mock_stream_ctx)
        mock_stream_ctx.__exit__ = MagicMock(return_value=False)
        mock_stream_ctx.text_stream = iter([])
        mock_anthropic.messages.stream.return_value = mock_stream_ctx

        client = ClaudeClient(api_key="test-key")
        list(client.stream_message("Hello", system="Be brief."))

        call_kwargs = mock_anthropic.messages.stream.call_args.kwargs
        assert call_kwargs["system"] == "Be brief."
