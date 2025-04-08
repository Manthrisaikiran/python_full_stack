'''What is Dictionary?

1. A Dictionary in python is declared by enclosing a comma-separated list of key-value pairs using curly braces {}.

2. Changeable (Mutable)

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

3. Duplicates Not Allowed, Dictionaries cannot have two items with the same key

4. Dictionaries are used to store data values in key:value pairs.

5. The values in the dictionary can be of any type, while the keys must be immutable like numbers, tuples, or strings.

6. Dictionary keys are case sensitive.



Dictionary Methods:

clear() Removes all the elements from the dictionary

copy() Returns a copy of the dictionary

get() Returns the value of the specified key

items() Returns a list containing a tuple for each key value pair

keys() Returns a list containing the dictionary's keys

pop() Removes the element with the specified key

update() Updates the dictionary with the specified key-value pairs

values() Returns a list of all the values in the dictionary'''




# sunny={"kiran":"names",1:"sai",11:True}
# print(sunny["kiran"])



# sunny={"kiran":"names",1:"sai",11:True}
# sunny["kiran"]="python"
# print(sunny)



# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# print(aswini.get("sno"))
# #print(aswini.keys())
# #print(aswini.values())
# #print(aswini.items())




# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# aswini.update({"food":"biryani"})
# print(aswini)


# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# aswini.update({"name":"bunny"})
# print(aswini)



# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# aswini.pop("name")
# print(aswini)
# # print(list(aswini))




# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# for bawarchi in aswini:
#     print(bawarchi)



# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# for bawarchi,pista_house in aswini.items():
#     print(bawarchi,pista_house)


# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# for bawarchi,pista_house in aswini.items():
#     print(bawarchi)
#another way..(or)
# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# for bawarchi in aswini:
#     print(bawarchi,aswini.get(bawarchi))



# phani={
#     1:"a",
#     2:"b",
#     3:{1:"aa"}
# }
# print(phani[3][1])