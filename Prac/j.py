# Problem: J. Digital Clock

# Input
minute_num = int(input())

# Calculation
hour_num = minute_num // 60
minute_remain = minute_num % 60

# Output
print(hour_num)
print(minute_remain)

# Alternative Solution
'''
print((m:=int(input()))//60,'\n',m%60,sep='')
'''
