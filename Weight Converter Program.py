# Exercise

Weight = input("Weight:")
Unit = input("(L)bs or (K)g:")

Units = Unit.upper()

if Units == 'L':
    weight = int(Weight)*0.453592
    msg = f'You are {weight} kilos'
    print(msg)
elif Units == 'K':
    weight = int(Weight)/0.453592
    msg = f'You are {weight} pounds'
    print(msg)

# OR

weight = int(input("Weight:"))
unit = input("(L)bs or (K)g:")

if unit.upper() == 'L':
    converted = weight * 0.453592
    print(f'You are {converted} kilos')

else:
    converted = weight / 0.453592
    print(f'You are {converted} pounds')
