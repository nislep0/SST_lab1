import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lab1 import evolve



def test_fail():
    initial_field = [
        ".....",
        "..x..",
        "..x..",
        "..x..",
        ".....",
    ]
    excepted = [
        ".....",
        "..x..",
        "..x..",
        "..x..",
        ".....",
    ]
    result = evolve(initial_field, 1)
    assert result == excepted




