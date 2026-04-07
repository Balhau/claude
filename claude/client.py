"""Core Claude API client wrapper."""

import os
from typing import Optional

import anthropic


class ClaudeClient:
    """A simple wrapper around the Anthropic Claude API."""

    DEFAULT_MODEL = "claude-opus-4-5"
    DEFAULT_MAX_TOKENS = 1024

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialise the ClaudeClient.

        Args:
            api_key: Anthropic API key. Falls back to the ANTHROPIC_API_KEY
                     environment variable when not provided.
            model: Model identifier to use for requests. Defaults to
                   ``DEFAULT_MODEL``.
        """
        self._api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self._api_key:
            raise ValueError(
                "An Anthropic API key must be provided either via the api_key "
                "argument or the ANTHROPIC_API_KEY environment variable."
            )
        self._client = anthropic.Anthropic(api_key=self._api_key)
        self.model = model or self.DEFAULT_MODEL

    def message(
        self,
        prompt: str,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        system: Optional[str] = None,
    ) -> str:
        """
        Send a single user message and return the assistant's response text.

        Args:
            prompt: The user message to send.
            max_tokens: Maximum number of tokens in the response.
            system: Optional system prompt.

        Returns:
            The text content of the assistant's response.
        """
        kwargs: dict = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            kwargs["system"] = system

        response = self._client.messages.create(**kwargs)
        return response.content[0].text

    def stream_message(
        self,
        prompt: str,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        system: Optional[str] = None,
    ):
        """
        Stream a single user message, yielding text chunks as they arrive.

        Args:
            prompt: The user message to send.
            max_tokens: Maximum number of tokens in the response.
            system: Optional system prompt.

        Yields:
            Text chunks from the assistant's streamed response.
        """
        kwargs: dict = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            kwargs["system"] = system

        with self._client.messages.stream(**kwargs) as stream:
            for text in stream.text_stream:
                yield text
