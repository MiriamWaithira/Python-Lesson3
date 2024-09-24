# Create a function called divisible_by_ten(), that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

# without lambda function
def divisible_by_ten(num): #function
    result = num % 10 #calculate the remainder when num is divided by 10
    if result == 0: #checking the condition
        return True
    else:
        return False
num = int(input('Enter a number:')) #The user to input a number
print(divisible_by_ten(num)) #The program to print the answer 

# with lambda function
divisible_by_ten = lambda num: 'True' if num % 10 == 0 else 'False'
num = int(input('Enter the number of choice:')) #The user to input a number
print(divisible_by_ten(num)) #The program to print the answer