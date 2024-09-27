# Problem: ZG. Underscores

# Input
string = input()

# Calculation
underscore_string = ""
length = len(string)
last_index = length - 1

for index, character in enumerate(string):
    underscore_string += character
    if index != last_index:
        underscore_string += '_'

# Output
print(underscore_string)

# Alternative Solution
'''
print('_'.join(input()))
'''

