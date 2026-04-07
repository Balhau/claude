import random
from mcp.server.fastmcp import FastMCP

FIRST_NAMES = [
    "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah",
    "Ivan", "Julia", "Kevin", "Laura", "Michael", "Nina", "Oscar", "Petra",
    "Quinn", "Rachel", "Samuel", "Tara", "Ursula", "Victor", "Wendy", "Xavier",
    "Yara", "Zane",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore",
    "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee", "Gonzalez",
    "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall", "Young",
    "Allen",
]

mcp = FastMCP("name-generator")


@mcp.tool()
def get_name() -> str:
    """Generate a random full name."""
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return f"{first} {last}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
