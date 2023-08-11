names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])   # index starts from 0
print(names[-2])    # second from last
print(names[2:])   # end of the list
print(names[2:4])
names[0] = 'jon'    # updating an item
print(names)

# Exercise
# printing the largest number in the list

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


