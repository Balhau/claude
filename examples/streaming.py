"""Example: streaming response from Claude."""

from claude import ClaudeClient


def main():
    client = ClaudeClient()

    print("Streaming response: ", end="", flush=True)
    for chunk in client.stream_message("Tell me a short joke."):
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
