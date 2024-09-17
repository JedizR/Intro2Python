# Problem: ZB. Three Middle Letters

# Input
string = input()

# Calculation
length = len(string)
mid = length // 2
start = mid - 1
end = mid + 2
answer_string = string[start:end]

# Output
print(answer_string)

# Alternative Solution
'''
print((a:=input())[len(a)//2-1:len(a)//2+2])
'''