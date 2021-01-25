
x = set('abcde')
y = set('bdxyz')

print('e' in x) # membership
print(x-y) #difference
print(x | y) #union
print(x & y) #intersection
print(x ^ y) #symmetric difference
print(x > y, x < y) #superset, subset

z = x.intersection(y) #find the same elements
z.add('SPAM')
print(z)


z.update(set(['X', 'Y'])) #update the set and add two elements
print(z)



z.remove('X') #delete one element
print(z)

print(y)

for item in y:
	print(item * 3)


''' Why sets?
	Set operations have a variety of common uses, some more practical than mathematical
'''
L=[1,2,3,1,1,3,4,5]
set(L)
L=list(set(L)) #remove duplicates
print(L)

#check if an elements exits in a set
print(7 in L)

