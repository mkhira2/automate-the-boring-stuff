# print('How many cats do you have?')
# numCats = input()
# if int(numCats) >= 4:
#     print('That is a lot of cats.')
# else:
#     print('That is not that many cats.')

print('How many cats do you have?')
def cats():
    numCats = input()
    try:
        if int(numCats) < 0:
            print('That\'s impossible.')
        elif int(numCats) >= 4:
            print('That is a lot of cats.')
        else:
            print('That is not that many cats.')
    except ValueError:
        print('Please enter a valid number.')
        cats()

cats()