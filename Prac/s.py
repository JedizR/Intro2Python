# Problem: S. Sum of Squares

# Input
num = int(input())

# Calculation
total = 0

for i in range(1, num + 1):
    total += i ** 2

# Output
print(total)

# Alternative Solution
'''
print(sum(i**2 for i in range(1,int(input())+1)))
'''