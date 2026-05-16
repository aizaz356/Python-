try:
    from test import get_area,output_parameter
except ImportError:
    pass

epsilon = 0.001  # precision needed

import math

def test_float():
    r = 2.0
    result = 12.566

    assert abs(get_area(r) - result) < epsilon

def test_int():
    r = 0
    result = 0

    assert abs(get_area(r) - result) < epsilon

def test_parameter_float():
    val = 1.0
    v, out = capture_output(output_parameter)(val)

    assert out.startswith("The parameter of the circle with radius 1.0 is 6.28")

# output capturing decorator
def capture_output(fn):                            # decorator function
    def wrapper(*args, **kwargs):                  # in decorator inner function(wrapper function)
        import sys                                 # sys is system specific paramters and functions
        from io import StringIO                    # bring io allow us to capture output
        orig_stdout = sys.stdout                   # save original output
        capturedOutput = StringIO()                # create a StringIO object to capture output
        sys.stdout = capturedOutput                # redirect stdout to the stringIO object

        v = fn(*args, **kwargs)                    # call the original function with its arguments

        sys.stdout = orig_stdout                   # restore original stdout(so normal print works again)
        output_val = capturedOutput.getvalue()     # print 'Captured', capturedOutput.getvalue()
        return v, output_val                       # return both: v(the function's actual return value), output_val(all captured output)
    return wrapper                                 # return the inner function 