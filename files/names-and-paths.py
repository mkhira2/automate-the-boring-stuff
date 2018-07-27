import os
# includes os.path.join ('folder1', 'folder2', 'folder3', 'file.png')
# instead of having to write 'folder1\\folder2\\folder3\\file.png'

print('c:\\spam\\eggs.png')
print(r'c:\spam\eggs.png')

path = 'c:\\folder1\\folder2\\spam.png'
path2 = '/Users/kenjihirabayashi/Desktop/automate-the-boring-stuff/'
print(os.getcwd()) # print current working directory

# print(os.chdir('/')) OSX # changes current working directory
# print(os.chdir('c:\\')) WINDOWS # changes current working directory

print(os.path.abspath('spam.png')) # prints absolute file path to directory

print(os.path.relpath(path, 'c:\\folder1')) # prints relative file path to directory

print(os.path.dirname(path)) # prints folder structure "c\f1\f2"

print(os.path.basename(path)) # prints file name "spam.png"

print(os.path.exists(path)) # returns boolean (does path exist?)

print(os.path.isfile(path)) # returns boolean (is final a file?)

print(os.path.isdir(path)) # returns boolean (is final a directory?)

# print(os.path.getsize(path)) # returns size in bytes as integer

totalSize = 0
for filename in os.listdir(path2):
	if not os.path.isfile(os.path.join(path2, filename)):
		continue
	totalSize = totalSize + os.path.getsize(os.path.join(path2, filename))

print(totalSize)

if not os.path.exists('Users/kenjihirabayashi/Desktop/parent/child'):
	os.makedirs('Users/kenjihirabayashi/Desktop/parent/child')

# spam.png = relative file path
# c\folder1\folder2\spam.png = absolute file path

# . = this directory
# .. = parent directory