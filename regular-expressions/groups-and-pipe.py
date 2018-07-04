import re

# Groups are created in regex strings with parentheses

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group()) # prints whole number

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1)) # prints area code
print(mo.group(2)) # prints number

# Pipes can match one of many possible groups

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group()) # prints batmobile

mo = batRegex.search('Batmotorcycle lost a wheel.')
print(mo == None) # prints true
# calling print(mo.group()) will throw an error here since mo == None