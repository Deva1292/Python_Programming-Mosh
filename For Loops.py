
for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(5, 10):   # range function prints the specified range of numbers
    print(item)

for item in range(5, 10, 2):   # the last digit 2 defines the steps ... this will print 5 7 9 with 2 steaps.
    print(item)

# Exercise

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total:{total}")
