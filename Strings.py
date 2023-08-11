course = '''
Hi John,
Here is our first email to you.
Thank You,
The support team
'''
print(course)


course = 'Python for Beginners'
        # 012345
another = course[:]
print(course[0])
print(course[-1])  # negative index will start from last character
print(course[0:3])  # returns characters starting from 0 to 2 not 3
print(course[0:])  # returns value till the end of the string
print(course[:5])  # ends till the 5th index from the start of the string
print(course[:])  # 0 is assumed as the start index, and it will end with the string
print(another)  # copy paste the exact value

#Exercise

name = 'Jennifer'
print(name[1:-1])  # will return the characters starting from index 1 ie. 2nd character
                   # all the way to the first character from the end but excluding the character at the last index