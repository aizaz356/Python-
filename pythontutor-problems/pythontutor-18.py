class Animal:        # A class is a template for objects
    legs = False     # member/class variable 
    name = ''
    
    def sound(self):  # function 
        return '*silence*'
    
    def move(self): 
        return True
        
        
a = Animal()
# e.g : b = a   so, in this the b is also a Animal instance        