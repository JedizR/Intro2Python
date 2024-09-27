# Problem: ZF. Is palindrome?

# Input
string = input()

# Calculation and Output
reverse_string = ""
length = len(string)

for character in range(length - 1 , -1, -1):
    reverse_string += string[character]

if reverse_string == string:
    print("YES")
else:
    print("NO")

# Alternative Solution
'''
print("YES" if (s:=input())==s[::-1] else "NO")
'''