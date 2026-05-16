from test import code_holder

def test_third():
    assert code_holder(15, 39) == 15+39

def test_negatives():
    assert code_holder(-12, -19) == -12 + -19