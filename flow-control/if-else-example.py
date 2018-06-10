# password = 'swordfish'
# if password == 'swordfish':
#     print('Access granted.')
# else: 
#     print('Wrong password.')

password = 'swordfish'
print('What is the password?')
attempt = input()
if attempt == password:
    print('Access granted.')
else:
    print('Wrong password.')