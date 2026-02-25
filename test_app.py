"""Tests for app.py"""
from app import greet


def test_greet_returns_hello():
    assert greet("World") == "Hello, World!"


def test_greet_with_name():
    assert greet("Claude") == "Hello, Claude!"
