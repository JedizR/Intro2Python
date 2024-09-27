# Problem: ZM. Of The Same Sign

# Input
n = int(input())
num_list = list(map(int,input().split()))

# Calculation
answer = "NO"
length = len(num_list)

for i in range(0, length - 1):
    if num_list[i] * num_list[i + 1] > 0:
        answer = "YES"
        break

# Output
print(answer)