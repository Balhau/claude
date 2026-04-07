"""Example: basic message exchange with Claude."""

from claude import ClaudeClient


def main():
    client = ClaudeClient()

    response = client.message("What is the capital of France?")
    print("Response:", response)


if __name__ == "__main__":
    main()
