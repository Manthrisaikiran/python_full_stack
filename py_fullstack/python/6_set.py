'''What is Set?

index

A set is a collection which is unordered, and unindexed.-

1. Set items are unordered, and do not allow duplicate values.

2. Unordered means that the items in a set do not have a defined order.

3. Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

4. A set is created by placing all the items (elements) inside curly braces {}, separated by comma, or by using the built-in set() function.

5. It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
'''

'''
Set Methods:

add() : Adds an element to the set

clear():Removes all the elements from the set

copy(): Returns a copy of the set

pop(): Removes an element from the set

remove(): Removes the specified element

update() :Update the set with another set, or any other iterable'''



# sunny={1,2,3,4,34}
# print(type(sunny))


# sunny={}""" if set is empty defult it will take dictionary"""
# print(type(sunny))


# sunny={1,2,3,4,34,2,22,11,10,9,55}''' set is unorder and does not take duplicate value '''
# print(sunny)



# sunny={1,2,3,4,34,2,22,11,10,9,55}
# sunny.add(50)"""add() set method"""
# print(sunny)


"""update() set method"""
# sunny={1,2,3,4,34,2,22,11,10,9,55}
# sunny.update({50,20,30,40,11,20,60,0})
# # sunny.update((50,20,30,40,11,20,60,0))''' we  can give any way it must ittarable'''
# # sunny.update([50,20,30,40,11,20,60,0])
# # sunny.update([50,20,30,40,11,20,60,0,"python"])
# print(sunny)



"""remove() set method"""

# sunny={-1,2,2,2,12,1,0,1,1,2,2,2,3,4,53,546,4}
# sunny.remove(546)
# # sunny.pop() 
# """pop is used to remove unordered element""" 
# print(sunny)


"""clear() set method """

# sai={1,22,33,0,44,6}
# sai.clear()
# print(sai)


"""copy() set method"""

# sai={1,22,33,0,44,6}
# manthri=sai.copy()#copied data already it will not reflect on sai adding data
# sai.add(66)
# print(sai)
# print(manthri)

'''
Set Operations


1.union() Return a set containing the union of sets

2.difference() Returns a set containing the difference between two or more sets

3.intersection() Returns a set, that is the intersection of two or more sets

4.isdisjoint() Returns whether two sets have a intersection or not

5.issubset() Returns whether another set contains this set or not

6.issuperset() Returns whether this set contains another set or not

7.symmetric_difference() Returns a set with the symmetric differences of two sets
'''

'''union() set operation'''

# set1={1,2,3,4,5}
# set2={4,6,7,8,4}
# print(set1.union(set2))

'''intersection() set operation'''
# set1={1,2,3,4,5,7}
# set2={4,6,7,8,4,7}
# print(set1.intersection(set2))


'''difference() set operation'''
# set1={1,2,3,4,5}
# set2={2,6,7,8,4}
# print(set1.difference(set2))


'''symmentric_difference() set operation. it is a opposite of intersection'''
# set1={1,2,3}
# set2={5,6,7,2}
# print(set1.symmetric_difference(set2))


'''isdisjoint() set operation. in this operation both set elements not equal'''

# set1={1,2,3,}
# set2={4,5,6,7}
# print(set1.isdisjoint(set2))


'''incase if set elements are same in set1 and set2'''
# set1={1,2,3,}
# set2={2,3,4,}
# print(set1.isdisjoint(set2))


'''issubset() set operation. subset= child, superset=parent'''

# set1={1,2,3}
# set2={1,2,3,4,5}
# print(set1.issubset(set2))

'''incase opposite set elements'''
# set1={1,2,3,4,5}
# set2={1,2,3}
# print(set1.issubset(set2))


'''issuperset() set operation. subset is opposite of superset'''
# set1={1,2,3,4,5}
# set2={1,2,3}
# print(set1.issuperset(set2))

'''incase opposite set elements'''
# set1={1,2,3,4,5}
# set2={1,2,3}
# print(set1.issuperset(set2))
 
 
 
'''using for loop'''

# for j in {1,2,3,24,4,45}:
#     if j==1:
#         print("true")
#         break
#     else:
#         print("flase")
        
        
        
        
"""frozenset()

The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.

Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

Due to this, frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is not ordered (the elements can be set at any index).

frozenset() means mutable set is converting into immutable set. if set is converted into frozen set no changes i will done"""


# h=[12,3,44,5]
# # print(type(h))
# d=frozenset(h)
# print(d)


'''changing frozenset to list,mutable'''
h=[12,3,44,5]
d=frozenset(h)
#print(d.append(123))
print(list(d))