# Basic string formatting example
format_string = 'Salama {}!'
print(format_string.format('Tompoko'))

# Allows multiple values to populate the string
name = "Solo"
age = 16
print(" I {} dia {} taona".format(name, age))

# Can specify an index for the substitution
format_string = "Hello {1} {0}, you got {2}%"
print(format_string.format('Smith', 'Carol', 75))

# Can use named substitutions, order is not significant
format_string = " I {artist} no mihira an'ilay hira mitondra ny lohateny hoe {song} izay nivoaka tamin'ny {year}"
print(format_string.format(artist='Wada sy Youngs', song='Mon amour taloha', year=2022))

print('|{:25}|'.format('25 characters width'))

print('|{:<50}|'.format('left aligned')) # Same as not specifying an alignment
print('|{:>25}|'.format('right aligned'))
print('|{:^25}|'.format('centered'))

# Can format numbers with comma as thousands separator
print('{:,}'.format(1234567890))
print('{:,}'.format(1234567890.0))