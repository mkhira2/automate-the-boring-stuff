print('range(4) ==> ' + str(range(4)))
print('list(range4) ==> ' + str(list(range(4))))
print('list(range(0, 100, 2) ==> ' + str((list(range(0, 100, 2)))))

#--------------------

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is ' + supplies[i])

#--------------------

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size)
print(color)
print(disposition)

#--------------------

firstName = 'kenji'
lastName = 'hirabayashi'

firstName, lastName = lastName, firstName

print('First name is(n\'t?): ' + firstName)
print('Last Name is(n\'t?): ' + lastName)