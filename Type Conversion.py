#Type Conversion

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)  #cannot subtract string and integer. '1982' is different from 1982 the number.
print(type(age))
print(age)

# whenever you use an input function, you always get a string. You should lways convert that string into an integer or float.

#Exercise

weight_pounds = input('Weight in Pounds: ')
weight_kg = int(weight_pounds) / 2.205
print(weight_kg)