print( "Hello dictionaries!")

# definition ---
dict = { 'apple': 23, 'banana': 45, 'choco': 100}
print( dict)
print( dict.get( 'apple'))
print( dict['apple'])

# adding ---
dict['test'] = 67
print( dict)

appleVld ='apple' in dict.keys()
print( 'apple' in dict.keys())
print( appleVld)

prise147Vld = 147 in dict.values()
print( prise147Vld)

# iterating ---
for key, value in dict.items():
    print( " * " + key + ": " + str(value))

