# If statement
num = 20
if num >= 20:
    print('The number is twenty')


# If...else statement
speed = 70
if speed > 20:
    print('Fast')
else:
    print('slow')


# If...elif...else
# If the condition evaluates to true, code block 1 is executed.
# If condition1 evaluates to false, then condition2 is evaluated.
# If condition 2 is true, code block 2 is executed.
# If condition 2 is false, code block 3 is executed.
grade = 92
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('Fail')