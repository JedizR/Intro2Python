# Problem: Z. Insert In the Middle

# Input
string = input()
letter = input()

# Calculation
length = len(string)
mid = length // 2
answer_string = string[:mid] + letter + string[mid:]

# Output
print(answer_string)

# Alternative Solution
'''
print((a:=input())[:len(a)//2]+input()+a[len(a)//2:])
'''