# Problem: T. Sum of n Numbers

# Input and Calculation
n = int(input())
total = 0

for i in range(n):
    total += int(input())

# Output
print(total)

# Alternative Solution
'''
print(sum(int(input()) for _ in range(int(input()))))
'''