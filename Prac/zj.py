# Problem: ZJ. Even Indices

# Input
n = int(input())
num_list = list(map(int, input().split()))

# Calculation and Output
print(*num_list[::2])