# Problem: ZE. Games

# Input
string = input()

# Calculation and Output
a_count = 0
b_count = 0

for character in string:
    if character == 'A':
        a_count += 1
    elif character == 'B':
        b_count += 1

if a_count > b_count:
    print('ALICE')
elif b_count > a_count:
    print('BOB')
else:
    print('DRAW')


# Alternative Solution
'''
print('ALICE' if ((a:=input()).count('A')) > (b:=a.count('B')) else 'BOB' if b > a.count('A') else 'DRAW')
'''