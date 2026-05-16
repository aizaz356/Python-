try:
    from math import sqrt, average, improve_guess
except ImportError:
    pass

epsilon = 1e-4  # precision needed

def test_avg_float():
    a = 0.1112
    b = 0.1113

    assert abs(average(a, b) - 0.11125) <epsilon


def test_avg_int():
    a = 1
    b = 2

    assert abs(average(a, b) - 1.5) < epsilon


def test_avg_int_2():
    a = 35112
    b = 35113

    assert abs(average(a, b) - 35112.5) < epsilon


def test_sqrt_int():
    v = 674
    assert abs(sqrt(v) - 25.9615) < epsilon


def test_improve_guess():
    n = 54
    g = 7.0  # haven't discussed casting yet. So, need to send at least one float
    res = improve_guess(n,g)
    assert abs(res - 7.3571) < epsilon


def test_improve_guess_zero():
    n = 1e-7
    g = 0 
    res = improve_guess(g,n)
    assert abs(res - 5.000000005) < epsilon


def test_improve_guess_2():
    # this one is for a student who can handle extremely bad cases
    # It can be done given the content we have covered already!
    n = 54
    g = 7
    res = improve_guess(g,n)
    assert abs(res - 7.3571) < epsilon


def test_improve_guess_2_dup():
    # due to increase weightage
    n = 54
    g = 7
    res = improve_guess(g,n)
    assert abs(res - 7.3571) < epsilon


# output capturing decorator
def capture_output(fn):                          # decorator function
    def wrapper(*args, **kwargs):                # in decorator inner function with arguments[(*args is Arbitrary positional arguments), (**kwargs is Arbitrary keyword arguments)]
        import sys                               # sys is system specific parameters and functions
        from io import StringIO                  # bring io allows us to capture output
        orig_stdout = sys.stdout                 # save original output
        capturedOutput = StringIO()              # create a StringIO object to capture output
        sys.stdout = capturedOutput              # redirect stdout to the StringIO object

        v = fn(*args, **kwargs)                  # call the original function with its arguments

        sys.stdout = orig_stdout                 # restore original output(so the normal print works again)
        output_val = capturedOutput.getvalue()   # print 'Captured', capturedOutput.getvalue()
        return v, output_val                     # return both: v(the function's actual return value), output_val(all captured output)
    return wrapper                               # return the inner function  
    
