try:
    from e01 import get_diag_sum
except ImportError:
    pass

def test_get_diag_sum_1():
    v = 0
    assert get_diag_sum(v) == None          # input = 0, output = None

def test_get_diag_sum_2():
    v = [18, 46, 86, 80, 158, 1490]
    for i in v:
        assert get_diag_sum(i) == None      # even input, output = None
        
def test_get_diag_sum_3():
    v = 25
    assert get_diag_sum(v) == 10761        # input = 25, output = 10761

def test_get_diag_sum_4():
    v = 159
    assert get_diag_sum(v) == 2692637      # input = 159, output = 2692637

def test_get_diag_sum_5():
    v = 1001
    assert get_diag_sum(v) == 669171001    # input = 1001, output = 669171001  