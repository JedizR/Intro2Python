# Problem: ZA. Swap Halves

# Input
string = input()

# Calculation
length = len(string)
mid = length // 2
answer_string = string[mid:] + string[:mid]

# Output
print(answer_string)

# Alternative Solution
'''
print((a:=input())[len(a)//2:]+a[:len(a)//2])
'''