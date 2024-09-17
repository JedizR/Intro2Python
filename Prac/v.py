# Problem: V. Number of Zeros

# Input and Calculation
n = int(input())
count = 0

for i in range(n):
    if int(input()) == 0:
        count += 1

# Output
print(count)

# Alternative Solution
'''
print(sum(int(input())==0 for _ in range(int(input()))))
'''