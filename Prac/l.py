# Problem: L. Three Chests

# Input
chest_1 = int(input())
chest_2 = int(input())
chest_3 = int(input())

# Calculation
if chest_1 <= chest_2 and chest_1 <= chest_3:
    total = chest_2 + chest_3
elif chest_2 <= chest_1 and chest_2 <= chest_3:
    total = chest_1 + chest_3
else:
    total = chest_1 + chest_2

# Output
print(total)

# Alternative Solution
'''
print(sum(sorted([int(input()),int(input()),int(input())])[1:]))
'''