# Writing elegant loops in programs using list comprehensions
# Using a for loop
nums = [4, -11, 23, 44, 17, -130]
doubled = []
for num in nums: #Iterates the whole list
    doubled.append(num * 2)
    print(doubled) # The output will be a list with doubled elements

# To achieve the same in one line, we use list comprehensions
nums = [4, -11, 23, 44, 17, -130]
doubled = [num * 2 for num in nums]
print(doubled) # The output will be a list with doubled elements


# The general Syntax of a list comprehension is as follows:
# new_list = [<expression> for <elements> in <collection>]