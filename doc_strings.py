# doc strings are used in python to comprehensively define a fn use in the fn itself
def greet_msg(name='Darth Vader', age=19):
    '''
    Info: Returns a greeting for a user
    '''
    return print(f'Hello {name}! You are {age}?')


greet_msg('Manan', 20)

# see the doc string
print(greet_msg.__doc__)
