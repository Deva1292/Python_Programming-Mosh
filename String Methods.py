# Methods

course = 'Python for Beginners'

print(len(course))
# len counts the number of characters in a string
# len is a general purpose function built into python
# course.upper() # dot operators are methods which are specific functions to a string
# general purpose functions do not belong to string or numbers or other kinds of objects

print(course.upper())  # changes to upper case
print(course)
print(course.lower())  # changes to lower case
print(course.title())  # changes to title case

print(course.find('P'))  # returns the index
print(course.find('O'))  # case-sensitive will return -1
print(course.find('Beginners'))  # will return the starting index of the word

print(course.replace('Beginners','Absolute Beginners'))  # replacing characters and words in a string
print(course.replace('beginners','Absolute Beginners'))  # case-sensitive # will not be replaced
print(course.replace('P','J'))

print('Python' in course)  # Check if the characters are present in the string # boolean Expression
print('python' in course)  # in method produces the boolean value
