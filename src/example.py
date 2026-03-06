"""Clean reference module — this file passes all enabled ruff rules."""

from __future__ import annotations


def greet(name: str, *, loud: bool = False) -> str:
    """Return a greeting string."""
    message = f"Hello, {name}!"
    if loud:
        message = message.upper()
    return message


def list_comprehension_demo(items: list[object]) -> list[str]:
    """Prefer list comprehension over map()."""
    return [str(item) for item in items]


if __name__ == "__main__":
    print(greet("Codespace", loud=True))  # noqa: T201
