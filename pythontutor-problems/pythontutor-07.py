def f(x):                     # name x used as formal parameter
    y = 1                     # local variable
    x = x + y
    print ('x =' , x)
    print ('p =' , p)         # global variable
    return x
    
p = 20
x = 3
y = 2
z = f(x)                      # value of x used as actual parameter

print('z ='  , z)
print('x ='  , x)
print('y ='  , y) 
