def fib(n):
    if n <= 1:      # same as if n == 0 or n == 1: but in short form if n <= 1:
        return n
    else:
        a = fib(n - 1)
        b = fib(n - 2)
        return a + b
    

v = fib(3)