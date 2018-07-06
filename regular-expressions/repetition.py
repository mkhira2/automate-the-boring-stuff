import re

#--------------------------
# Must match optional filter 0 or 1 time ()?

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # prints Batman

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # prints Batwoman

mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo == None) # prints True

#--------------------------
# Phone Regex without optional filter

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo == None) # prints True because no area code is given

#--------------------------
# Phone Regex with optional filter

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo == None) # prints False because area code is optional

#--------------------------
# Must Match optional filter 0 or more times ()* 

batRegex = re.compile(r'Bat(wo)*man') # will find all below

print(batRegex.search('The Adventures of Batman'))
print(batRegex.search('The Adventures of Batwoman'))
print(batRegex.search('The Adventures of Batwowowoman'))

#--------------------------
# Must Match optional filter 1 or more times ()+

batRegex = re.compile(r'Bat(wo)+man') # None / Match / Match

print(batRegex.search('The Adventures of Batman'))
print(batRegex.search('The Adventures of Batwoman'))
print(batRegex.search('The Adventures of Batwowowoman'))

#--------------------------
# Must Match optional filter n number of times {n}

haRegex = re.compile(r'(Ha){3}') # Simple example
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}') # Where it helps
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())

#--------------------------
# Must Match optional filter between x-y number of times {x,y}

haRegex = re.compile(r'(Ha){3,5}')

mo = haRegex.search('He said "HaHaHa"') # match
print(mo.group())

mo = haRegex.search('He said "HaHaHaHa"') # match
print(mo.group())

mo = haRegex.search('He said "HaHaHaHaHa"') # match
print(mo.group())

mo = haRegex.search('He said "HaHaHaHaHaHa"') # matches first 5, excludes final Ha
print(mo.group())

#--------------------------
# Greedy vs Non Greedy searches
# By default, Python is greedy and will return the first longest matching available value

digitRegex = re.compile(r'(\d){3,5}') # greedy match
mo = digitRegex.search('1234567890')
print(mo.group()) # prints 12345

digitRegex = re.compile(r'(\d){3,5}?') # ? denotes non greedy match
mo = digitRegex.search('1234567890')
print(mo.group()) # prints 123