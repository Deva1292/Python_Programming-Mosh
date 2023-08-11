numbers = [5, 2, 1, 7, 4]

numbers.append(20)  # inserts a number at the end
print(numbers)

numbers.insert(0, 10)  # inserts a number in an index
print(numbers)

numbers.remove(10)  # removes a particular value
print(numbers)

numbers.clear()  # doesn't take any values. just simply empties the list
print(numbers)

numbers.pop()  # remove the last item in the list
print(numbers)

numbers.index(5)  # checks the existence of a value in the list
print(numbers)
print(numbers.index(50))   # shows error
print(50 in numbers)  # will get a boolean value

numbers.sort()  # sorts the list (ascending order
print(numbers)

numbers.reverse()  # reverses the sorted list (descending order)
print(numbers)

numbers2 = numbers.copy()   # make a copy of the list
numbers.append(10)
print(numbers2)
print(numbers)


# Exercise
# remove the duplicates in a list

numbers = [2, 4, 8, 5, 4, 5, 4, 8]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
