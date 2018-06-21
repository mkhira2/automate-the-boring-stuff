import copy

# This will cause cheese to de-reference spam and become its own entity
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
# cheese and spam will be different
print(cheese)
print(spam)