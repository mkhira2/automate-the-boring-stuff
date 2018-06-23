myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage combination', 42: 'The Answer'}
print(spam)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}

print([1, 2, 3] == [3, 2, 1]) # will evaluate to false
print(eggs == ham) # will evaluate to true

print('name' in eggs)
print('name' not in eggs)

print('eggs keys are: ' + str(list(eggs.keys())))
print('eggs values are: ' + str(list(eggs.values())))
print('eggs items are: ' + str(list(eggs.items())))

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

print('cat' in eggs.values())

if 'color' in eggs:
    print(eggs['color'])

print(eggs.get('age', 0))
print(eggs.get('color', 'no color provided'))

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')

print(eggs.setdefault('color', 'black'))
print(eggs.setdefault('color', 'orange'))