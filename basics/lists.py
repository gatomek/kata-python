print( "Hello lists!")

# list introduction --------------------------

lst = ['anna',3,['hello', 'hi']]
print( len(lst))
print( len( lst[0]))

print( len( lst[2]))
print( lst)

# adding --------------------------

lst.append( 'test')
print( lst)

lst.insert(0, 'intro')
print( lst)

lst2 = [0,1,2]
lst3 = lst + lst2
print( lst3)

lst3.extend( [90,91,92])
print( lst3)

# removing --------------------------
lst3.remove( 0)
print( lst3)

# reversing --------------------------
lst3.reverse()
print( lst3)

# sorting --------------------------
lst4 = [6,3,8,9,2,4]
lst4.sort()
print( lst4)

lst4.sort( reverse=True)
print( lst4)

# indexing --------------------------
print( lst4.index( 8))
print( lst4.index(8,0))