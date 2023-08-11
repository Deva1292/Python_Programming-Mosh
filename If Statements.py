# if it's hot
# it's a hot day
# Drink plenty of water
# otherwise if it's cold
# it's a cold day
# Wear warm clothes
# otherwise
# it's a lovely day

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold :
    print("It's a cold Day")
    print("Wear warm clothes")
else:
   print("It's a lovely Day")

print("Enjoy your Day")

#  Exercise

price = 1000000

has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down Payment: ${down_payment}")
