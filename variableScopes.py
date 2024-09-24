# There are 4 scopes of variables that are associated with python functions
# Local scopes, Enclosing scopes, Global scopes, Built-in scopes

# Local scopes: Variables created inside a function. They are only accessible within that function.
def add_nums(a, b):
    answer = a + b #Local variable inside the function
    return answer
print(add_nums(2,13))


# Enclosing scopes: Variables in the local scope of enclosing (outer) functions. They are accessible to nested (inner) functions.
def add_nums(a, b): #outer function
    answer = a + b #Enclosing variable

    def double_it(): #inner function
        double = answer * 2 #local variable
        print(double) #will print 30
    double_it() #calling the inner function
    return answer
print(add_nums(2, 13)) #will print 15


# Global scope: Variables defined at the top level of a script or module, or declared global inside a function. They are accessible throughout the module.
var = 13 # Global variable
def addition(var, d): #Outer function
    total = var + d #Enclosing variable
    
    def square_it(): #inner function
        square = total * total #local variable
        print(square) #will print 225
    square_it() #calling the inner function
    return total
print(addition(var, 2)) #will print 15


# Built-in scope: Reserved keywords that Python uses for its built-in functions, such as print, def, for, in, len, sum
def length_is():
    print(len([7, 8, 9, 1]))  # Built-in function 'len'
length_is() #The output is 4