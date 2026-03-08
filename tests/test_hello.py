import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.hello import say_hello

def test_say_hello():
    assert say_hello() == "Hello World"