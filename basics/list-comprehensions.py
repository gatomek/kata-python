print( "Hello list comprehensions!")

lst = [x for x in range(3)]
print( lst)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
options = [{'label': day, 'value': day} for day in days if day not in [ 'Sat', 'Sun']]
print(options)