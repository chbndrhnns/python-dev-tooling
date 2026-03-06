"""Tests for example module."""

from src.example import greet, list_comprehension_demo


def test_greet_normal() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_loud() -> None:
    assert greet("World", loud=True) == "HELLO, WORLD!"


def test_list_comprehension_demo() -> None:
    result = list_comprehension_demo([1, 2, 3])
    assert result == ["1", "2", "3"]
