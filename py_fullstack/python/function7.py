'''
a function is a block of code which only runs whenit is called
{
    ....
    ....
    ....
}


syntax of function

Function name
      ^
      . parameters
      .     ^
      .     .
      .     .
      .     .
      .     .
def my_sum(a, b):    #Function definition
return a + b         #Function definition



Function call ---> my_sum(10, 20)
                           ^   ^
                           .   .
                           .   .
                           .   .
                         arguments

Parameters are mentioned in the function definition.

Actual parameters(arguments) are passed during a function call

By the help of function call we can reduce the time ,space of writing code,readability 

'''

# def sai():                                     #}function def
#     print("this is function")#function body    #}
# sai()   #function call

'''single parameter function'''
# def sai(aa): 
#     print("this is function",aa)
# sai(100)



'''multiple parameter function'''
# def sai(aa,b,c): 
#     print("this is function",aa,b,c)
# sai(100,30,40)

'''.....................................'''
# def sai(aa,b,c):
#     a=1
#     b=2
#     print(a+b)
# sai(100,22,33)


# def sai(a,b):
#     print(a+b)
    
# sai(100,22)
# sai(10,20)



'''we can call function any tmes using loops'''
# def sai(a,b):
#     print(a+b)
    
# while True:
#     sai(10,21)


'''input can send this way'''
# def lakshmi(name):
#     print("hi",name)
# n=input("enter the name:")
# lakshmi(n)  



'''by using "*"(aribitory argument) multiple data in the arguments can store in the parameter.it can store in the form of tuple '''
# def kiran(*name):
#     print("hi",name)
# kiran(1,2,3,4,7,8,544,3)


''' by using the "**"(keyword argument)  multiple data in arguments can store in the parameter. it can store in the form of dictionary  " '''
# def kiran (**name):
#     print("hi",name)
# kiran(name="ram",age=25)

'''using square backets. it can store in the form of list'''
# def kiran(name):
#  print("hi",name)
# kiran([1,2,3,4,7,8,544,3])


"nestted function ..> function with in a function "
# def outer_function():
#     print("this is outer function")
#     def inner_function():
#         print("this is inner function")
#     inner_function()
# outer_function()


'''7.1_function linking file'''
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)    

'''7.1_function linking file line 9 to 11. use of return is to get wanted data only '''
# def add(a,b):
#     return(a+b)



"""
Lambda Function

A lambda function is a small anonymous function.
A lambda function reduce the code size
A lambda function can take any number of arguments, but can only have one expression.

  #keyword
     ^
     .
     . # a  is a argument
     . # a*a is a one-line expression
f = lambda a:a*a

# f is afunction object that accepts and stores the result of the expression.
"""


# x=lambda a,b,c:a+b+c
# print(x(5,2,1))


# l1=[12,34,56,78]
# l2=[]
# for i in l1:
#   t=lambda a:a+1
#   l2.append(t(i))
# print(l2)



# a='kiran'
# s=lambda d:d*10
# print(s(a))



"""....................advanced function..................."""
"""
filter() method

The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax:

filter(function, sequence)

Parameters:
function: function that tests if each element of a sequence true or not.
sequence: sequence which needs to be filtered, it can
be sets, lists, tuples, or containers of any iterators.
Returns: returns an iterator that is already filtered
"""


# ages=[5,12,17,18,24,32]
# def myFunc(x):
#   if x >=18:
#    return True 
#   else:
#     return False
# sai=filter(myFunc,ages)
# print(list(sai))



"""map(function,iterable)
  
  the python map() function is used to resturn a list of results.
  after applying a given function to each item of an iterable(list,tuple etc..)
  by using of map function data will change based on input
  """
# def calculateAddition(n):
#     return n+n
# number=(1,2,3,4)
# result=map(calculateAddition,number)
# print(list(result))

'''diff b/w filter and map ex pg'''
# def even(x):
#   if x%2==0:
#     print(x)
# nums=[11,22,33,44,55]
# # map=list(map(lambda x: x**2,nums))
# # print(list(map))
# filter=list(filter(lambda x: x%2==0,nums))
# print(filter)



"""
  reduce() function
  the reduce() turns a singleyfunction,as the name describes,applies a given function to the iterables and return a single value.
  """
# from functools import reduce
#   #reduce(function,sequence)
# d=reduce(lambda a,b:a+b,[23,21,45,98])
# print(d)


"""Generator-function : a generator function is defined like a normal function,
but whenever it needs to generate a value,
it does so with the yield keyword rather than return.
if the body of a def contains yield, the function automatically becomes a generator function
"""

# def simpleGeneratorfun():
#     yield 1
#     yield 2
#     yield 3
# ## x is a generatormobject
# x= simpleGeneratorfun()
# ##iterating over the generator object using next
# print(x.__next__())##in python 3, __next__()
# #print(x.__next__())
# ##print(x.__next__())


"""the yield statement is responsible for controlling the flow of the generator function. 
it pauses the function execution by saving all states and yield to caller.
later it resumes execution when a successive function is called.we can use the multiple yield statement in generator function.

* return : the return  statement returns a value and terminates the whole function and only one return statement canbe used inthe function.
ex: 
"""
# def aa():
#      return 1+1
#      return 2+1 # this function not executed 
# print(aa())


# def suresh(a,b):
#   print(a*b*a*b*a)
# suresh(1,2)