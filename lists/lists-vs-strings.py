# Lists are mutable
# String are immutable

# Mutable list example
spam = [0, 1, 2, 3]
cheese = spam
cheese[1] = 'Hello!'
# cheese and spam will be the same
print(cheese)
print(spam)

# Immutable string example
spam = 'spam'
cheese = spam
# cheese[1] = 'Hello!' will throw an error "'str' does not support item assignment'"
# Instead...
newCheese = cheese[0] + 'Hello!' + cheese[2:4]
# cheese and newCheese will be different
print(cheese)
print(newCheese)

#----------EXAMPLE----------#
def eggs(cheese):
    cheese.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)