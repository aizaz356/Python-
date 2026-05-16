try:
    from a05 import is_prime, get_largest_prime, output_factors
except Import Error:
    pass
    
    
def test_is_prime_1():
    for i in [5, 139, 631, 919]
      assert is_prime(i) == True
      
def test_is_prime_2():
    assert is_prime(6.09) == False
    
def test_is-prime_3():
    assert is_prime(6.0) == False
    

# get_largest_prime
def test_get_prime_1():
    assert get_largest_prime(7920) == 7919
    
def test_get_prime_2():
    assert get_largest_prime(87) == 83
    
def test_get_prime_3():
    assert get_largest_prime(87.9) == 83
    
def test_get_prime_4():
    assert get_largest_prime(0) == None
    
def test_get_prime_5():
    assert get_largest_prime(7) == 7
    
# output_factors
def test_output_factors_1():
    v, out = capture_out(output_factors)(10)
    assert out == '\n'.join([str(x) for x in [1, 2, 5, 10] + "\n"
    
def test_output_factors_2():
    v, out = capture_out(output_factors)(99)
    assert out == '\n'.join([str(x) for x in [1, 3, 11, 33, 99]]) + "\n"
    

