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




