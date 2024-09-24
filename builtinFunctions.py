# Built-in functions in Python are pre-defined functions that are always available in the Python interpreter.
# These functions are part of Python's standard library and can be used without importing any additional modules.


# Example program utilizing multiple built-in functions

# 1. Taking input from the user and converting it to an integer
num = int(input("Enter an integer: "))

# 2. Finding the absolute value using abs()
absolute_value = abs(num)
print(f"The absolute value of {num} is {absolute_value}")

# 3. Finding the square of the number using pow() (also equivalent to num ** 2)
square = pow(num, 2)
print(f"The square of {num} is {square}")

# 4. Converting the number to a string using str()
num_str = str(num)
print(f"The number as a string is: {num_str}")

# 5. Getting the length of the string representation using len()
length = len(num_str)
print(f"The length of the number string is: {length}")

# 6. Creating a list of numbers and finding the sum using sum(), max, and min()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
print(f"Sum of the list: {total_sum}")
print(f"Maximum value in the list: {maximum}")
print(f"Minimum value in the list: {minimum}")

# 7. Sorting the list in descending order using sorted()
sorted_numbers = sorted(numbers, reverse=True)
print(f"Sorted list in descending order: {sorted_numbers}")

# 8. Using the round() function to round a floating-point number
float_num = 3.14159
rounded_num = round(float_num, 2)
print(f"Rounded number (to 2 decimal places): {rounded_num}")

# 9. Using type() to display the type of an object
print(f"The type of {float_num} is {type(float_num)}")
print(f"The type of {numbers} is {type(numbers)}")