import re

phoneSentence = '512-555-1234 and 972-555-1234 are the same number in different cities. 210-555-1234 is in a different state.'

# without groups - returns list of strings
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall(phoneSentence))

# with groups - returns list of tuples, and tuples have strings
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(phoneSentence))

lyrics = '12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, and 1 Partridge in a Pear Tree'

xmasRegex = re.compile(r'\d+\s+\w+')
print(xmasRegex.findall(lyrics))

# creating our own character classes

robocopSentence = 'Robocop eats baby food.'

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(robocopSentence))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall(robocopSentence))

consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall(robocopSentence))
