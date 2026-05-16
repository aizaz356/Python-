try:
    from e01 import get_diag_sum
except ImportError:
    pass

def test_get_diag_sum_1():
    v = 0
    assert get_diag_sum(v) == None        # input = 0, output = None     

def test_get_diag_sum_2():
    v = [2, 4, 6, 8, 10, 1090]
    for i in v:
        assert get_diag_sum(i) == None    # even input, output = None

def test_get_diag_sum_3():
    v = 5
    assert get_diag_sum(v) == 101         # input = 5, output = 101

def test_get_diag_sum_4():
    v = 15
    assert get_diag_sum(v) == 2381        # input = 15, output = 2381
