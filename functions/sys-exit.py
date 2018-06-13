import sys, pyperclip # import multiple modules with comma separator

pyperclip.copy('Hello')
print(pyperclip.paste())
sys.exit()
print('Goodbye') # this will never run