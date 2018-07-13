import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello world!')) # True
print(beginsWithHelloRegex.search('Hi world!')) # False

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!')) # True
print(endsWithWorldRegex.search('Hello planet!')) # False

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('2349872982')) # True
print(allDigitsRegex.search('23498xxx72982')) # False

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# dot star comin atcha

name = 'First Name: Kenji Last Name: Hirabayashi'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(name))