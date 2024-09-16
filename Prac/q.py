# Problem: Q. Cakes and Bags

# Input
apple_cake_num = int(input())
orange_cake_num = int(input())
bag_1 = int(input())
bag_2 = int(input())

# Calculation and Output
if bag_1 > bag_2:
    if apple_cake_num > orange_cake_num:
        if bag_1 >= apple_cake_num and bag_2 >= orange_cake_num :
            print("YES")
        else:
            print("NO")
    else:
        if bag_1 >= orange_cake_num and bag_2 >= apple_cake_num :
            print("YES")
        else:
            print("NO")
else:
    if apple_cake_num > orange_cake_num:
        if bag_2 >= apple_cake_num and bag_1 >= orange_cake_num :
            print("YES")
        else:
            print("NO")
    else:
        if bag_2 >= orange_cake_num and bag_1 >= apple_cake_num :
            print("YES")
        else:
            print("NO")