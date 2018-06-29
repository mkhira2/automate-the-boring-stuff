print("That is Alice's cat.")
print('That is Alice\'s cat.')

print('Hello there!\nHow are you?\nI\'m fine.') # will escape
print(r'Hello there!\nHow are you?\nI\'m fine.') # r prefix will print backslashes

print("""Dear Alice,
    Eve's cat has been arrested for catnapping, cat burglary, and extortion.
    Sincerely,
    Bob.""")

spam = 'Hello world!'
print(spam[0])
print(spam[-1])

print('Hello' in spam) # true

print('HELLO' in spam) # false