# (x,y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,2)
# (1,3)

for x in range(4):  # outer loop
    for y in range(3):  # inner loop
        print(f'({x},{y})')

# Exercise

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    print('x' * x_count)

    # or

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)