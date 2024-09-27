# Problem: ZK. Even Elements

# Input
n = int(input())
num_list = list(map(int, a:=input().split()))

# Calculation and Output
for element in num_list:
    if element % 2 == 0:
        print(element, end=" ")