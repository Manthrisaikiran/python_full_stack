'''Arrays:

Arrays in Python are Data Structures that can hold multiple values of the same type. 
Often, they are misinterpreted as lists or Numpy Arrays. 
Technically, Arrays in Python are distinct from both these'''

import array as arr

#defining the array

a=arr.array('d',[1.1,1.2,3.2])

# #adding the element

# a.append(2.5)

# print(a)


## extend the array list
# a.extend([2.2,3.2])

# print(a)


## removing the element using the pop operation
print(a.pop(1))