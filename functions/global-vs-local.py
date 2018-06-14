def spam():
    eggs = 'Hello'
    print('eggs is ' + eggs) # prints Hello

eggs = 42
spam()

# ------------------- #

def spam():
    print('eggs is ' + str(eggs)) # prints 42

eggs = 42
spam()
