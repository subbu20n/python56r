#set -set is mutable. but inside the set elements are immutable, unorderd, finite, unique elements
#set1 = {2, 3, (3, 4), 'str1', frozenset([8, 9]), 3, 2, [2,4,5]} 
#print(set1) 

#----SET--- (mutable)----inside the set are elements are (immutable) -- possible to 
set1 = {2, 3, (3, 4), 'str1', frozenset([8, 9,10]),  2, 2, 9 }
print(set1) 

#set1[3] = 'subbu' # we cant do reassignment (set is mutable only inside elements we cant change  immutable)
print(set1)

#   -----Frozenset-----==> Immutable ,inside also immutable 

fset1 = frozenset([1,3,5,8,9,'str1'])
print(fset1)
fset1[2] = '10'


