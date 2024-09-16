# Problem: M. Lucky Number

# Input
num = int(input())

# Calculation and Output
if not num % 7 and num % 11:
    print("YES")
else:
    print("NO")