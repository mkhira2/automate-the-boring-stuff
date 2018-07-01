import pyperclip

# upper case
spam = 'Hello world!'
print(spam.upper())

# remember - strings are immutable:
print(spam)
spam = spam.upper()
print(spam)

# lower case
spam = 'Hello world!'
print(spam.lower())

# title case
spam = 'hello world!'
print(spam.title())

spam = 'Hello world!'
print(spam.islower()) # returns false

spam = 'hello world'
print(spam.islower()) # returns true

spam = 'HELLO WORLD'
print(spam.isupper()) # returns true

spam = ''
print(spam.isupper()) # returns false - needs one upper

spam = ''
print(spam.islower()) # returns false - needs one lower

# chaining methods:
print('Hello'.upper().isupper()) # returns true
print('hello'.isalpha()) # true - consists of only letters
print('hello123'.isalpha()) # false - contains letters and numbers
print('hello123'.isalnum()) # true - contains letters and numbers
print('123'.isdecimal()) # true - returns numbers
print('        '.isspace()) # true - contains only spaces
print('This Is Title Case'.istitle()) # true - contains only title casing
print('Hello world!'.startswith('H')) # true - starts with H
print('Hello world!'.endswith('world!')) # true - ends with world!

# join list of strings together
print(', '.join(['cats', 'rats', 'bats'])) # cats, rats, bats

# split strings
print('My name is Simon'.split()) # splits on whitespace by default
print('My name is Simon'.split('m')) # splits on 'm', returns all but 'm'

spam = 'Hello'

print(spam.rjust(10)) # right justify - returns '     Hello'
print(spam.rjust(10, '*')) # returns '*****Hello'
print(spam.ljust(10)) # left justify - returns 'Hello     '
print(spam.ljust(10, '-')) # returns 'Hello-----'

print(spam.center(20)) # returns '        Hello       '
print(spam.center(20, '=')) # returns '========Hello========'

spam = '     Hello     '

print(spam.strip()) # strip all whitespace
print(spam.lstrip()) # strip all whitespace on right
print(spam.rstrip()) # strip all whitespace on left

print('SpamSpamBaconSpamEggsSpamSpam'.strip('Spam'))

spam = 'Hello there!'
print(spam.replace('e', 'XYZ')) # replaces 'e' with 'XYZ'

pyperclip.copy('Hello!!!!!!!!!!')
print(pyperclip.paste())