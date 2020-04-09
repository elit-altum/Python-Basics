# exercise to display password for user

username = input('Enter username: ')
password = input('Enter password: ')

print(f'Your username is: {username}')

password_length = len(password)
secret_password = '*' * password_length

print(f'{secret_password} is {password_length} digits long')