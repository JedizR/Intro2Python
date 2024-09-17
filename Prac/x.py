# Problem: X. Incorrect A + B

# Input
num_1 = input()
num_2 = input()

# Calculation
wrong_answer = num_1 + num_2
correct_answer = int(num_1) + int(num_2)

# Output
print(wrong_answer, correct_answer)

# Alternative Solution
'''
print((a:=input())+ (b:=input()), int(a)+int(b))
'''