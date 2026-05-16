try:
    from a04 import get_grade, calculate_sgpa
except:
    pass

epsilon = 1e-3  # precision needed

def test_grade_float_1():
    score = 89.50
    assert get_grade(score) == 'A+'


def test_grade_float_2():
    score = 89.49
    assert get_grade(score) == 'A'


def test_grade_float_3():
    score = 89.1
    assert get_grade(score) == 'A'


def test_grade_float_4():
    score = 49.49
    assert get_grade(score) == 'F'



def test_sgpa_int_1():
    assert abs(calculate_sgpa('nothing', 'F', 'nothing') - 0) < epsilon


def test_sgpa_int_2():
    assert abs(calculate_sgpa('nothing', 'A', 'nothing') - 4.0) < epsilon


def test_sgpa_int_3():
    assert abs(calculate_sgpa('nothing', 'B+', 'A') - 3.665) < epsilon


def test_sgpa_int_4():
    assert abs(calculate_sgpa('C-', 'B+', 'nothing') - 2.5) < epsilon
    
    
def test_sgpa_int_5():
    assert abs(calculate_sgpa('C-', 'D+', 'nothing') - 1.5) < epsilon


def test_sgpa_int_6():
    assert abs(calculate_sgpa('nothing', 'nothing', 'nothing') - 0) < epsilon
    
    
def test_sgpa_int_7():
    assert abs(calculate_sgpa('D+', 'nothing', 'B+') - 2.33) < epsilon
    
    
def test_sgpa_int_8():
    assert abs(calculate_sgpa('C-', 'nothing', 'B+') - 2.5) < epsilon
    
    
# output capturing decorator
def capture_output(fn):                          # decorator function
    def wrapper(*args, **kwargs):                # in decorator inner function with arguments[(* args is Arbitrary positional arguments),(**kwargs is Arbitrary keyword arguments)]
        import sys                               # sys is system specific parameters and functions
        from io import StringIO                  # bring io allow us to capture output
        orig_stdout = sys.stdout                 # save original output
        CapturedOutput = StringIO()              # create a string IO object to capture output
        sys.stdout = CapturedOutput              # redirect stdout to the string IO object

        v = fn(*args, **kwargs)                  # call the original function with its arguments

        sys.stdout = orig_stdout                 # restore original output(so the normal print works again)
        output_val = CapturedOutput.getvalue()   # print 'Captured', capturedOutput.getvalue()
        return v, output_val                     # return both: v(the function's actual return value), output_val(all captured output)
    return wrapper                               # return the inner function





