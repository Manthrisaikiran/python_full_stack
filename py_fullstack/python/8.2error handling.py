"""What is Error Handling?

What is an Exception?

An exception is an error that happens during execution of a program.

When that error occurs, Python generate an exception that can be handled, which avoids your program to crash.

Why use Exceptions?

Exceptions are convenient in many ways for handling errors and special conditions in a program. When you think that you have a code which can produce an error then you can use exception handling.
Compile-Time Errors

Errors that occur when you violate the rules of writing syntax are known as Compile-Time errors. This compiler error indicates something that must be fixed before the code can be compiled. All these errors are detected by the compiler and thus are known as compile-time errors.

Missing symbols like ..()

Printing the value of variable without declaring it

Missing colon (terminator)

Run-Time Errors

Errors which occur during program execution(run-time) after successful compilation are called run-time errors. One of the most common run-time error is division by zero also known as Division error. These types of error are hard to find as the compiler doesn't point to the line at which the error occurs
try:

{

Run this code

except:

{

Execute this code when there is an exception

else:

{

No exceptions? Run this code.

finally:

{

Always run this code."""


# try:
#     #print(a)
#     print("a")
# except:
#     print("error vachindhi")
# else:
#     print("error raledhu")
# finally:
#     print("always")


# try:
#     print('a'+10)
# except:
#     print("error occured")


'''to know what error is occured'''
# try:
#     print('a'+10)
# except Exception as kiran:
#     print("error occured",kiran)


# try:
#     print('a'+10)
#     print(a)
# except TypeError:
#     print("type error occured")
# except NameError:
#     print("name error occured")



'''multiple exception handling'''

# try:
#     print('a'+10)
# except:
#     print("outer")
#     try:
#         print(a)
#     except:
#         print("linner")Different types of Errors


'''DIFFERENT TYPES OF ERRORS

AttributeError:Raised by syntax obj.foo, if obj has no member named foo

EOFError:Raised if "end of file" reached for console or file input

IOError:Raised upon failure of I/O operation (e.g., opening file)

IndexError:Raised if index to sequence is out of bounds

KeyError:Raised if nonexistent key requested for set or dictionary

KeyboardInterrupt:Raised if user types ctrl-C while program is executing

NameError:Raised if nonexistent identifier used

Stoplteration:Raised by next(iterator) if no element; see Section 1.8

TypeError:Raised when wrong type of parameter is sent to a function

ValueError:Raised when parameter has invalid value (e.g., sqrt(-5))

Zero Division Error: Raised when any division operator used with 0 as divisor'''




'''types of errors and overcome way'''

##type error:

# s=str(1)+'s' # s=1+'d' 
# print(s)



##key error:

# d={1:'a'}
# print(d[2])



#index error:

# c=[1,2,3,5,82389,232]
# print(c[100])


#key board interrupt: while running the program if enter anything inthe terminal

# while True:
#     print('loop')




#syntax error:

# d=[1,2,37,67,3
#    print(d)
   
   
  
#FileNotFoundError:
   
# f=open("kiran.txt",mode="r")




#ModuleNotFoundError:

# import safghjjtrhxc




# valueError:
    
# c=int(input())
# print(c)





# ZeroDivisionError:
    
# print(1/0)



# AttributeError:
    
# i=1000000
# i.append(100)



# TypeError: func() takes 1 positional argument but 2 were given

# def func(a):
#     print(a)
# func(1,2)