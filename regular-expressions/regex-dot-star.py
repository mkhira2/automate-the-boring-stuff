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

# 5.00