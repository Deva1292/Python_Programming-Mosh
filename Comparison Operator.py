# if temperature is greater than 30
# it's a hot day
# otherwise if it's less than 10
# it's a cold day
# otherwise
# it's neither hot nor cold

temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# == equality operator
# >=  <=  <  >
# != not equal

#  Exercise

name = input("Enter your name")
character = len(name)  # len counts the number of characters in a string

if int(character) < 3:
    print("Name must be at least 3 characters")
elif int(character) > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good!")