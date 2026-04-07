# claude

A lightweight Python client for the [Anthropic Claude](https://www.anthropic.com/claude) API.

## Features

- Simple `message()` call for one-shot prompts
- `stream_message()` for streaming responses
- Optional system prompt support
- API key resolution from environment variable or argument

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Set your API key:

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

### Single message

```python
from claude import ClaudeClient

client = ClaudeClient()
response = client.message("What is the capital of France?")
print(response)
```

### Streaming

```python
from claude import ClaudeClient

client = ClaudeClient()
for chunk in client.stream_message("Tell me a short joke."):
    print(chunk, end="", flush=True)
print()
```

### System prompt

```python
response = client.message(
    "Translate 'hello' to Spanish.",
    system="You are a professional translator.",
)
print(response)
```

## Examples

See the [`examples/`](examples/) directory for runnable scripts.

## Development

```bash
pip install -r requirements-dev.txt
pytest
```
