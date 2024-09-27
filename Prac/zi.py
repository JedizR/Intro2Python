# Problem: ZI. Increase Elements

# Input
n = int(input())
num_list = list(map(int, input().split()))
increase_by = int(input())

# Calculation
for i, element in enumerate(num_list):
    num_list[i] += increase_by

# Output
print(*num_list)