# Create a function named large_power(), that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False.
# without lambda function
def large_power(base, exponent):
    # Calculate base to the power of exponent
    result = pow(base, exponent)
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False
# Test cases
print(large_power(2, 13))  # True, because 2^13 = 8192 which is greater than 5000
print(large_power(2, 12))  # False, because 2^12 = 4096 which is less than 5000
print(large_power(6, 5))   # True, because 6^5 = 7776 which is greater than 5000
print(large_power(5, 5))   # False, because 5^5 = 3125 which is less than 5000


# with lambda function Trial-1
large_power = lambda base, exponent: pow(base, exponent) > 5000
# Test cases
print('\n',large_power(2, 13))  # True, because 2^13 = 8192 which is greater than 5000
print(large_power(2, 12))  # False, because 2^12 = 4096 which is less than 5000
print(large_power(6, 5))   # True, because 6^5 = 7776 which is greater than 5000
print(large_power(5, 5))   # False, because 5^5 = 3125 which is less than 5000


# with lambda function Trial-2
large_power = lambda base, exponent: 'True' if pow(base, exponent) > 5000 else 'False'
# Test cases
print('\n',large_power(2, 13))  # True, because 2^13 = 8192 which is greater than 5000
print(large_power(2, 12))  # False, because 2^12 = 4096 which is less than 5000
print(large_power(6, 5))   # True, because 6^5 = 7776 which is greater than 5000
print(large_power(5, 5))   # False, because 5^5 = 3125 which is less than 5000
