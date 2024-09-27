# Problem: ZD. Press F to Pay Respects

# Input
string = input()

# Calculation
count_f = 0

for character in string:
    if character == 'f':
        count_f += 1

# Output
print(count_f)

# Alternative Solution
'''
print(input().count('f'))
'''