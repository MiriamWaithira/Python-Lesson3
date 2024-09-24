# For loops using range
welcome_message = 'Welcome to Python'
for i in range(5): # The message will be printed 5 times
    print(welcome_message)


# While loops
# A while loop performs a set of instructions as long as a given condition is true.
count = 0
while count <= 2:
    #The loop body
    print(count)
    count += 1 #The output starts from 0 to 2


# Loop controls: Break and continue
# The break statement is used to terminate the loop immediately when it is encountered.

# Using for loop
colors = ['blue', 'green', 'white', 'orange', 'violet', 'brown']
color_i_want = 'white'
for color in colors:
    if color == color_i_want:
        print('They have the color you want')
        break
    print(color) #The loop will print the statement instead of white and stop

# Using while loop
colors = ['blue', 'green', 'white', 'orange', 'violet', 'brown']
color_i_want = 'white'
length = len(colors) #To know how many colors there are
count = 0 #Used to compare against length there is
while count < length:
    print(colors[count])
    if colors[count] == color_i_want:
        print('They have the color I want')
        break
    count += 1 #The loop will print upto white and stop
    #and 'They have the color I want' statement


# Python continue Statement
# The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.
# In this example, Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
ages = [13, 24, 17, 36]
for age in ages:
    if age < 21:
        continue
    print(age) #Only ages above 21 will be printed


# Nested Loops- Loops that are nested inside other loops
# Nested loops can be used to access items of lists which are inside other lists.
# The item selected from the outer loop can be used as the list for the inner loop to iterate over.
groups = [['Paul', 'Samuel'], ['Ahmed', 'Gregory'], ['Karl', '']]
# The outer loop will iterate over each list in the groups list
for group in groups:
    # This inner loop will go through each name in each list
    for name in group:
        print(name) #All names in all lists will be printed