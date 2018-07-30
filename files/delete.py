import os, shutil, send2trash

# gets current working directory
print(os.getcwd())

# removes EMPTY directories
os.rmdir('C:\\Users\\mkhir\\Desktop\\delicious_directory')

# removes directories and contents
shutil.rmtree('C:\\Users\\mkhir\\Desktop\\delicious_directory') 

# performing a dry run before deleting
for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename) 
        print(filename)

# safer method (sends to trash instead of hard delete) 
send2trash.send2trash('C:\\Users\\mkhir\\Desktop\\delicious.txt')