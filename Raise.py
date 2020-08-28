#Raise in Python
# a = input("What 's your name\n")
# b = input('How much you earn ?\n')

# if b == 0:
#     raise ZeroDivisionError('b is Zero so stopping the program')

# if a.isnumeric():
#     raise Exception('Numbers are not allowed')

# print('Hello {a}')

c = input('Enter your name make sure first word must be Capital \n')

try:
    print(a)

except Exception as e:
    if c == 'Amit':
        raise ValueError('Amit is not allowed because Harry is Blocked')
    print(f'Hey {c} Welcome in our Company')
