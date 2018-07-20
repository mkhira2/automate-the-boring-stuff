import re

# SUB METHOD 

namesRegex = re.compile(r'Agent \w+')

print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # prints ['Agent Alice', 'Agent Bob']

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')) # prints "REDACTED gave...to REDACTED"

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # prints ['A', 'B']

print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')) # prints "Agent A**** gave...to Agent B****"

# VERBOSE MODE

