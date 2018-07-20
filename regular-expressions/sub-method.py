import re

# SUB METHOD 

namesRegex = re.compile(r'Agent \w+')

print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # prints ['Agent Alice', 'Agent Bob']

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')) # prints "REDACTED gave...to REDACTED"

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # prints ['A', 'B']

print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')) # prints "Agent A**** gave...to Agent B****"

# VERBOSE MODE lets you add whitespace and comments to the regex string passed to re.compile()

verboseNumberRegex = re.compile(r'''
\d\d\d # area code
- # first dash
\d\d\d # first 3 digits
- # second dash
\d\d\d\d # last 4 digits
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

print(verboseNumberRegex.findall('My office number is 512-555-1234x678'))