# Program specification
"""
Replace the comment in the following code with a while loop.

num_x = int(input('How many times should I print the letter
X? '))
to_print = ''
#concatenate X to to_print num_x times
print(to_print)

"""

num_x = int(input('How many times should I print the letter X? '))
to_print = ''

counter = 0
while counter < num_x:
    to_print += "x"
    counter += 1

print(to_print)