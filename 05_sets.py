a = {1,2,3,4,5,1}
print(a) #if we use repetative number the set will ignore
a = {}
print(type(a)) #this will create empty dictionary and not empty sets
# to create empty set following syntax is used
b = set()
print(type(b))
# methods of sets
# 01 adding values to the sets
b.add(5)
b.add(6)
b.add(9)
b.add(4)
# b.add([4,5,6]) you cannot add list and dictornary to a set because list is not hasable
# we can add tuples in a list because it is hasable
print(b)
# 02  b.len(b) this can find the lenth of the sets
print(len(b))
# 03 b.remove(jo remove krna h)this can remove the element from the set
b.remove(5)
print(b)
# 04 b.pop() this will random value from the set
b.pop()
print(b)