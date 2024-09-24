# A function that adds numbers
# def add_nums():
#     print(2+13+14)


# Calling a function
def add_nums():
    print(2+13+14)
#calling the function
add_nums()


# Function Arguments/ Parameters
# Information can be passed into functions as arguments.
# Arguments make our functions more dynamic and reusables.
def add_nums(a, b, c):
    answer = a + b + c
    return answer
#assign function call to a variable called total
total = add_nums(2, 13, 14)
print('Total:', total)


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
#If the number is unknown
def add_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
    # Call the function and print the result outside of it
total = add_nums(2, 3, 5)
print('The Total is:', total)


# Arbitrary Keyword Arguments, **kwargs
# If the keyword arguments to be passed in a function are not known, you should add ** before the parameter name in the function definition
# A function add_age() taking kwargs **age to calculate the sum of different people's ages.
def add_ages(**ages):
    sum = 0
    for k, v in ages.items():
        sum += v
    return sum
total_age = add_ages(Jane=23, John=23, Jack=26, Ahmed=22)
print('Their Total age is:', total_age)