# Problem: O. Pairs of Socks

# Input
left_sock_num = int(input())
right_sock_num = int(input())

# Calculation and Output
if left_sock_num < right_sock_num:
    print(left_sock_num)
else:
    print(right_sock_num)
    
# Alternative Solution
'''
print(min(int(input()), int(input())))
'''