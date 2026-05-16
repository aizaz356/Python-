try:
    from test import get_area, output_parameter
except ImportError:
    pass

epsilon = 0.001  # precision needed

import math 

def test_floats():
    vals = [2.0, 2.9, 1.9, 22.0, 3.09]

    for v in vals: assert abs(get_area(v) - (math.pi * v * v)) < epsilon    # for each radius(v)

def test_parameter_float():
    val = 1.999
    v, out = capture_output(output_parameter)(val)
    
    assert out.startswith("The parameter of the circle with radius 1.999 is 12.560")

# output capturing decorator
def capture_output(fn):                         #decorator function
    def wrapper(*args, **kwargs):               # in decorator inner function with arguments[(*args is Arbitrary positional arguments),(**kwargs is Arbitrary keyword arguments)]                                           
        import sys                              # sys is sysyem specific parameters and functions
        from io import StringIO                 # bring io allows us to capture output
        orig_stdout = sys.stdout                # save original output
        capturedOutput = StringIO()             # create a StringIO object to capture output
        sys.stdout = capturedOutput             # redirect stdout to the SringIO object
        
        v = fn(*args, **kwargs)                 # call the original function with its arguments

        sys.stdout = orig_stdout                # restore original stdout(so normal print works again)
        output_val = capturedOutput.getvalue()  # print 'Captured', capturedOutput.getcalue() 
        return v, output_val                    # return both: v(the function's actual return value), output_val(all cpatured output)
    return wrapper                              # return the inner function 
                                                                                       
                                               