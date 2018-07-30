import shutil

# copies spam file to delicious directory
shutil.copy('c:\\spam.txt', 'c:\\delicious')

# copies and renames files to delicious directory
shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')

# copies directory, including all files within
shutil.copytree('c:\\delicous', 'c:\\delicious_backup')

# moves file to new directory, removing old location
shutil.move('c:\\spam.txt', 'c:\\delicious\\walnut')

# to rename a file, move to same directory and specify new name
shutil.move('c:\\delicious\\walnut\\spam.txt', 'c:\\delicious\\walnut\\eggs.txt')