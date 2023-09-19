# Printing pout some strings containing quotes
print("Anio ilay andro")
print('hozy teniny hoe "Salama" daholy')

# Concatenataing strings together
string_1 = 'Mafinaritra'
string_2 = " ny Andro"
string_3 = string_1 + string_2
print(string_3)
print(len(string_3))

my_variable = 'Koto'
print(my_variable)
my_variable = "Nivo"
print(my_variable)

# A multi line string
z = """
Salama
tompoko
"""
print(z)

# Printing the type of a string - its class string
my_variable = 'Koto'
print(type(my_variable))

# Accessing parts of a string
my_string = 'Salama daholy'
print(my_string[4])
print(my_string[1:5])
print(my_string[:5])
print(my_string[2:])

# Converting a string to uppper case
print(z.upper())

print(type(b'abc')) # b -> bytes manova an'ilay abc ho byte

# Splitting a string up
title = 'Ny Tsara, Ny Ratsy, ary ny Maharikoriko'
print('Source string:', title)
print('Split using a space')
print(title.split(' '))
print('Split using a comma')
print(title.split(','))
 

# Counting howmany times a substring appears in a string
my_string = 'Count, the number     of spaces'
print("my_string.count(' '):", my_string.count(' '))

# String replacement / substitution
welcome_message = 'Salama daholy!'
print(welcome_message.replace("Salama", "Veloma"))

# Generating multiple strings
print('*' * 10)
print('Hi' * 10)

# Testing strings containing another string
print('Rakoto Ralay Rabe'.find('Rakoto'))
print('Mainty Raolona Ratefy'.find('Mainty'))

print('Rakoto' == 'Rakoto') # prints True
print('Rakoto' == 'Rabe') # prints False
print('Rakoto' != 'Rabe') # prints True
print('Rakoto' == 'rakoto') # prints False

# Various different string operations
some_string = 'Salama Daholy'
print('Testing a String')
print('-' * 20)
print('some_string', some_string)
print("some_string.startswith('S')", some_string.startswith('S'))
print("some_string.startswith('s')", some_string.startswith('s'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())

# String conversions
print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase()) #contraire Title
print('String leading, trailing spaces', "   xyz   ".strip())

# Adding a number to a string - need to use the str() function
msg = 'Manahoana Pela! raika amby roapolo taon ianao e =>' + str(21)
print(msg)
