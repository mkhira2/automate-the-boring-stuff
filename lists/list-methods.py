spam1 = ['hello', 'hi', 'howdy', 'heyas']
print('spam 1 is ' + str(spam1.index('hello')))			

spam2 = ['cat', 'dog', 'bat']
spam2.append('moose')
print('spam 2 is ' + str(spam2))

spam3 = ['cat', 'dog', 'bat']
spam3.insert(1, 'chicken')
print('spam3 is ' + str(spam3))

spam4 = ['cat', 'bat', 'rat', 'elephant']
spam4.remove('bat')
print('spam 4 is ' + str(spam4))

spam5 = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam5.remove('cat')
print('spam 5 is ' + str(spam5))

spam6 = [2, 5, 3.14, 1, -7]
print('spam 6 is ' + str(spam6.sort()))

spam7 = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print('spam 7 is ' + str(spam7.sort(reverse=True))) 

spam8 = [1, 2, 3, 'Alice', 'Bob']
print('spam 8 is ' + str(spam8.sort()))

spam9 = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam9.sort()
print('spam 9 is ' + str(spam9))

spam10 = ['a', 'z', 'A', 'Z']
spam10.sort(key=str.lower)
print('spam 10 is ' + str(spam10))