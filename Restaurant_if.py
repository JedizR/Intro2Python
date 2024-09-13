cash = float(input())
print('''O------------------------O
|  Jedi's Pizzeria Menu  |
O------------------------O''')
if cash >= 500:
    print('| (1) Golden Pizza - 500 |')
if cash >= 400:
    print('| (2) Pepperoni    - 400 |')
if cash >= 300:
    print('| (3) Hawaiian     - 300 |')
if cash >= 200:
    print('| (4) Plain Cheese - 200 |')
else:
    print('|  Sorry you are broke!  |')

print('''|                        |
O------------------------O''')
choice = input('What do you want? ')
if choice == '1':
    cash-=500
    print('you bought Golden Pizza!')
elif choice == '2':
    cash-=400
    print('you bought Pepperoni!')
elif choice == '3':
    cash-=300
    print('you bought Hawaiian!')
elif choice == '4':
    cash-=200
    print('you bought Plain Cheese!')
print(f'you have {cash} left!')