import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lab1 import evolve

def test_evolve():
    generation = 3
    initial_field = [
        "........",
        "..x.....",
        "..x.....",
        "..x.....",
        "........",
    ]
    exp = [
        "........",
        "........",
        ".xxx....",
        "........",
        "........",
    ]
    result = evolve(initial_field, generation)
    assert result == exp

def test_evolve_no_change():
    initial_field = [
        ".....",
        "..x..",
        "..x..",
        "..x..",
        ".....",
    ]
    result = evolve(initial_field, 0)
    assert result == initial_field 

def test_evolve_still_life():
    initial_field = [
        "......",
        ".xx...",
        ".xx...",
        "......",
    ]
    exp = [
        "......",
        ".xx...",
        ".xx...",
        "......",
    ]
    result = evolve(initial_field, 5)
    assert result == exp

def test_evolve_oscillator():    
    initial_field = [
        ".....",
        "..x..",
        "..x..",
        "..x..",
        ".....",
    ]
    exp = [
        ".....",
        ".....",
        ".xxx.",
        ".....",
        ".....",
    ]
    result = evolve(initial_field, 1)
    assert result == exp

def test_full_evolution():
    initial_field = [
            "xxx",
            "...",
            "...",
        ]
    exp = [
            "xxx",
            "xxx",
            "xxx",
        ]
    result = evolve(initial_field, 1)
    assert result == exp


