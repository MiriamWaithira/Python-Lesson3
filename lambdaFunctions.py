# A lambda function is a special type of function without a name.
# That is why it's referred to as an anonymous function.
# Lambda - is a keyword in Python for defining the anonymous function.
# argument(s) - any value passed to the lambda function
# expression - expression is executed and returned
snack = lambda : print('Njugu')
snack() #calling the lambda


# A lambda function with arguments
# Lambda function can take any number of arguments but can only have one expression.
# without the lambda function
def num_square(num):
    return num **2 #calculating the square
print('Square of num is:', num_square(8)) #calling the square function

#with the lambda function
num_square = lambda num: num **2 #the lambda function accepts the argument named num
print('Square of num is:', num_square(6)) #the lambda function has been called


# A palindrome is a word, phrase, number, or any sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
# A program that determines whether a given string is a Palindrome.
# without the lambda function
def isPalindrome(string):
    if (string == string[::-1]):
        return 'A Palindrome.'
    else:
        return 'Not a Palindrome.'
string = input('Enter a string:') #The user will input a string
print(isPalindrome(string)) #calling the function

#with the lambda function
isPalindrome = lambda string : 'A Palindrome.' if string == string[::-1] else 'Not a Palindrome.'
string = input('Enter the string:')
print(isPalindrome(string))