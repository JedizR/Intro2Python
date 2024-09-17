# Problem: P. Score Interpretation

# Input
score = int(input())

# Calculation and Output
if score > 80:
    print("Achieved")
elif score > 40:
    print("Developing")
else:
    print("Emerging")
    
# Alternative Solution
'''
print("Achieved"if(s:=int(input()))>80 else"Developing"if s>40 else"Emerging")
'''