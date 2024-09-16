# Problem: U. Print Even Numbers From A to B

# Input
start = int(input())
end = int(input())

# Calculation and Output
for i in range(start, end + 1):
    if i % 2:
        continue
    print(i)