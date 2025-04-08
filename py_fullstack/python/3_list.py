#krishna=[] #empty list
# print(type(krishna))


# krishna=list() #built in functon in list
# print(type(krishna))


# sai=[1,2.2,"python",True]#method1
# sai1=list([1,2.2])#method2
# print(type(sai))
# print(sai1)


#indexing examples:

# sandeep=[2.2,3.4,5.5,1,2,3,4,5]
# print(sandeep[2])




# sandeep=[2.2,3.4,5.5,1,2,3,4,5]
# print(sandeep[-1])





#slicing examples: [start:stop:skip]

# kiran=[7,3,5,3,34,64,"True"]
# print(kiran[0:5])



# kiran=[7,3,5,3,34,64,"True"]
# print(kiran[0:5:2])    #[start:stop:skip]




# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[0:5:3])




# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[5:0:-2])




# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[-1:-8:-2])




# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[5:0])



# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[5:0:-2])



# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[0:5+1])



# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[:5])



# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[5:])


# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[:])


# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[:-1])



# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# print(kiran[::-1])



# kiran=[7,3,5,3,34,64,2.4,32,5,35,39]
# kiran[1]="sai"
# print(kiran)

"""list methods"""

# sai=[1,2,3,4,4525,23,63,63,6]
# #variable.method()
# sai.append(123)
# print(sai)



# sai=[1,2,3,4,4525,23,63,63,6]
# #variable.method()
# sai.append([123])
# print(sai)


# sai=[1,2,3,4,4525,23,63,63,6]
# #variable.method()
# sai.extend([123])
# print(sai)




# sai=[1,2,3,4,4525,23,63,63,6]
# print(sai.count(63))



# sai=[1,2,3,4,4525,23,63,63,6]
# print(sai.index(4525))



# sai=[1,2,3,4,4525,23,63,63,6]
# print(len(sai))



# sai=[1,1,2,3,4,4525,23,63,63,6]
# sai.clear()
# print(sai)


# sai=[1,2,3,4,4525,23,63,63,6]
# a=sai
# print(a==sai)


# sai=[1,2,3,4,4525,23,63,63,6]
# a=sai
# print(id(sai))
# print(id(a))
# print(a==sai)



#no changes in after the copy example:

# sai=[1,2,3,4,4525,23,63,63,6]
# b=sai.copy()
# sai.append("abc")
# print(b)



# sai=[1,1,2,3,4,4525,23,63,63,6]
# sai.insert(0,"kiran")#index,data
# print(sai)



# sai=[1,1,2,3,4,4525,23,63,63,6]
# sai.pop(0)#index
# print(sai)



#removing....

# sai=[1,1,12,3,4,4525,23,63,63,6]
# sai.remove(12) #element
# print(sai)


# sai=[1,1,12,3,4,4525,23,63,63,6]
# sai.remove(1) #element
# print(sai)


#reversing data...
# sai=[1,1,12,3,4,4525,23,63,63,6]
# sai.reverse()
# print(sai)


#ascending order...
# c=[1,3,4,4,421,42,4231,4,442,4]
# c.sort()#small to  big
# print(c)


#decending order....
# c=[1,3,4,4,421,42,4231,4,442,4]
# c.sort(reverse=True)#big to small
# print(c)



# list compherension.....by the help of this we can write the code in single line
#[expression for iteam in  iterable]

# list=["even" if i % 2==0 else "odd" for i in range(10)]# syntax: [expresson if conditon for item in sequence]
# print(list)



# fruits=["apple","bananna","cherry","kiwi","mango"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)


#without using list compression...example1 only

# newlist=[]
# for x in ["apple","bananna","cherry","kiwi","mango"]:
#     if "a" in x:
#         newlist.append(x)
#         print(newlist)



# s=[1,2,3,4,3,4]
# for i in range(len(s)):
#     if s[i]==3:
#         print(i)



# str1=[1,6,6,6,6,6,6,6,6,6,6,6,6,2,4,5,5,6,3,3]
# n=[]
# for i in str1:
#     if i==6:
#         str1.remove(6)
#     else:
#         n.append(i)
#         print(n)




#how to remove multiple elements in list

## using list comprehension
# num=[1,2,3,4,5,6,7,8,9,10]
# num_to_remove=[1,3,5,7,9]
# #create new list using list comprehension
# num=[i for i in num if i not in num_to_remove]
# print(num)