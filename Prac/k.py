# Problem: K. School Announcement

# Input
temp = int(input())

# Calculation and Output
if temp > 35:
    print("CANCEL SCHOOL")
elif temp > 30:
    print("CANCEL TWO CLASSES")
else:
    print("NORMAL CLASSES")
    
# Alternative Solution
'''
print("CANCEL SCHOOL"if(t:=int(input()))>35 else"CANCEL TWO CLASSES"if t>30 else"NORMAL CLASSES")
'''