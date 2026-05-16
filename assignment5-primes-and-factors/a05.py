## IMPORTS GO HERE

## No imports needed

## END OF IMPORTS


#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#### END OF MARKER 

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def output_factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
#### END OF MARKER

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def get_largest_prime(n):
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return None
#### END OF MARKER


if __name__ == '__main__':
    print(is_prime(499))         # should return True
    print(output_factors(10))    # should output 1, 2, 5, 10 (one on each line)
    print(get_largest_prime(10)) # should return 7 

    