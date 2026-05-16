try:
    from a06 import output_prime_factors, get_nth_prime
except ImportError:
    pass

def output_prime_factors_1():
    v, out = capture_output(output_prime_factors)(23)
    assert out == '\n'.join([str(x) for x in [23]]) + "\n"

def output_prime_factors_2():
    v, out = capture_output(output_prime_factors)(230)
    assert out == '\n'.join([str(x) for x in [2, 5, 23]]) + "\n"

def output_prime_factors_3():
    v, out = capture_output(output_prime_factors)(230.6)
    assert out == '\n'.join([str(x) for x in [3, 7, 11]]) + "\n"


# get_nth_prime

def test_get_nth_prime_1():
    out = get_nth_prime(1)
    assert out == 1

def test_get_nth_prime_2():
    out = get_nth_prime(2)
    assert out == 3

def test_get_nth_prime_3():
    out = get_nth_prime(3)
    assert out == 5

def test_get_nth_prime_4():
    out = get_nth_prime(4)
    assert out == 7

def test_get_nth_prime_5():
    out = get_nth_prime(5)
    assert out == 11

def test_get_nth_prime_6():
    out = get_nth_prime(2.1)
    assert out == None

def test_get_nth_prime_7():
    out = get_nth_prime(29)
    assert out == 109

# output capturing decorator
def capture_output(fn):
    def wrapper(*args, **kwargs):
        import sys
        from io import StringIO
        orig_stdout = sys.stdout
        CapturedOutput = StringIO()
        sys.stdout = CapturedOutput

        v = fn(*args, **kwargs)

        sys.stdout = orig_stdout
        output_val = CapturedOutput.getvalue()
        return v, output_val
    return wrapper