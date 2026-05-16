try:
    from a07 import calculate_sgpa, calculate_sgpa_weighted
except ImportError:
    pass

epsilon = 1e-2 = 0.01      # precision needed

# calculate_sgpa

def test_calculate_sgpa_1():
    assert calculate_sgpa(['A', 'A-', 'A-', 'D+']) == 3.1675

def test_calculate_sgpa_2():
    assert calculate_sgpa(['C+', 'B', 'D', 'C', None]) == None

def test_calculate_sgpa_3():
    assert calculate_sgpa(['P', 'A', 'C-', 'D+', 'C']) == None

def test_calculate_sgpa_4():
    assert calculate_sgpa(['D', 'A', 'C-', 'D+', 1.0]) == None

def test_calculate_sgpa_5():
    assert calculate_sgpa(['A', 'B', 'C', 'D']) == 2.5

def test_calculate_sgpa_6():
    assert calculate_sgpa(['C+', 'B+', 'C-', 'D+']) == 2.165

def test_calculate_sgpa_7():
    assert calculate_sgpa(['A', 'B-', 'C-', 'D+']) == 2.4175

def test_calculate_sgpa_8():
    assert abs(calculate_sgpa(['D+', 'A-', 'B+', 'D+', 'C+', 'A-', 'A+', 'D+', 'C+']) -2.59) < epsilon





def test_calculate_sgpa_2_1():
    assert calculate_sgpa(None) == None

def test_calculate_sgpa_2_2():
    assert calculate_sgpa('A+') == 4.00

def test_calculate_sgpa_2_3():
    assert calculate_sgpa('D+') == 1.33
    
def test_calculate_sgpa_2_4():
    assert calculate_sgpa('C-') == 1.67






# calculate_sgpa_weighted

def test_calculate_sgpa_weighted_i_1():
    assert calculate_sgpa_weighted('D+', 4) == 1.33       # 'D+' grade, 4 credit hours

def test_calculate_sgpa_weighted_i_2():
    assert calculate_sgpa_weighted('C-', 3) == 1.67       # 'C-' grade, 3 credit hours

def test_calculate_sgpa_weighted_i_3():
    assert abs(calculate_sgpa_weighted(['D+', 'C-'], [3, 4]) - 1.52) < epsilon     # 'D+' grade for 3 credit hours, 'C-' grade for 4 credit hours

def test_calculate_sgpa_weighted_i_4():
    assert calculate_sgpa_weighted(['A', 'D-'], [1]) == None    # 'A' grade for 1 credit hour, 'D-' grade is invalid

def test_calculate_sgpa_weighted_i_5():
    assert calculate_sgpa_weighted(['A'], [1, 6]) == None       # 'A' grade for 1 credit hour, but credit hours list has 2 values

def test_calculate_sgpa_weighted_i_6():
    assert calculate_sgpa_weighted(['D+', 'A-', 'C+', 'G'], [3, 3, 1, 2]) == None    # 'D+', 'A-', 'C+' grades for 3, 3, and 1 credit hours respectively, but 'G' is an invalid grade

def test_calculate_sgpa_weighted_i_7():
    assert calculate_sgpa_weighted(['T', 'A-', 'C+', 'G'], [3, 3, 1, 2]) == None   # 'T', 'A-', 'C+' grades for 3, 3, and 1 credit hours respectively, but 'T' and 'G' are invalid grades

def test_calculate_sgpa_weighted_i_8():
    assert abs(calculate_sgpa_weighted(['B+', 'A-'], [4, 2]) - 3.44) < epsilon   # 'B+' grade for 4 credit hours, 'A-' grade for 2 credit hours





# output capturing deocorator
def capture_output(fn):                          # decorator function
    def wrapper(*args, **kwargs):                # in decorator inner function with arguments[(*args is Arbitrary positional arguments, **kwargs is Arbitrary keywors arguements)]
        import sys                               # sys is system-specific parameters and functions
        from io import StringIO                  # bring io allow us to capture output
        orig_stdout = sys.stdout                 # save/store original output
        CapturedOutput = StringIO()              # create a StringIO object to captured output
        sys.stdout = CapturedOutput              # redirect stdout to the StringIO object

        v = fn(*args, **kwargs)                  # call the original function with parameters

        sys.stdout = orig_stdout                 # restore original output(so the normal print works again)
        output_val = CapturedOutput.getvalue()   # Print 'Captured', CapturedOutput.getvalue()
        return v, output_val                     # return both:(the function's actual return value), output_val(all captured output)
    return wrapper                               # return the inner function





