# Problem: W. Missing Hero

# Input and Calculation
n = int(input())
total_hero = n * ( n + 1 ) // 2
found_hero = 0

for i in range(n-1):
    found_hero += int(input())

missing_hero = total_hero - found_hero

# Output
print(missing_hero)

# Alternative Solution
'''
print((n:=int(input()))*(n+1)//2-sum(int(input()) for _ in range(n-1)))
'''