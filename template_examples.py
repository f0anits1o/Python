import string

# Initialise the template with variables that
# will be substitute with actual values
template = string.Template('$artist sang $song in $year')

# Replace substitute variables with actual value
# Can use a key : value pair that indicates the values to replace
print(template.substitute(artist='Hosana', song='Tokatrano Sambatra', year=2020))
print(template.substitute(artist='Ampifitia', song='Eny', year=2019))
print(template.substitute(artist='Koraita', song='Aoreno ny finoana', year=2018))

# Using a dictionary to provide the value for the template variables
d = dict(artist = 'TMI', song='Fantatrao ny amiko', year = 2021)
print(template.substitute(d))

# Optionally providing only some of the template variable values
# print(template.substitute(artist='David Bowie', song='Rebel Rebel'))
print(template.safe_substitute(artist='Karmela', song='Mifampitantana'))
#tsy misy year io farany io.