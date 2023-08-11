#formatted string

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder' # string concatenation
msg = f'{first} [{last}] is a coder'  # formatted string # with the curly braces we are defining holes in our string
# which are filled with value of variables
print(message)
print(msg)