'''               object oriented programming    '''              
#class(template)
'''
1. we will define class by using 'class' keyword
2.blue print to create a objects
3.collection of objects is called class
'''
#ex furits




# object
#physical entity(real)
'''
1.an instance of a class
2. memory is create when it declared
'''
# ex apple,bananna,mango




# syntax

# class greetings():#class=class keyword,greetings=class name,
#     print("hello")#class body



# attribute(variable) data members
'''
age=20
color='blue'
'''



#method(behaviour) or functions, member functions
'''
eat()
sleep()
'''



#self keyword
'''
we can access the atributes and methods of the class(current class only)
'''

# class kiran():
#     def output():
#         print("this is class")
#     output()



#implementation function call using object call
# class kiran():
#     def output(self):
#         print("this is class")
# #object name= class name() object creation
# sai=kiran()
# sai.output()




# class shiva():
#     a=10
#     def show(self):
#         print("this is class")
# #obj name= class name
# kiran=shiva()
# print(kiran.a)
# kiran.show()



# class sri():
#     a=10
#     def classMethod(self):
#         print("this is class")
# #obj=class name()
# krian1=sri()
# kiran=sri()
# kiran.classMethod()
# print(kiran.a)




# class kiran():#class keyword class name
#     a=10#data member
#     def output(self):#method(self)
#         print(self.a)
# obj=kiran()#declaring of object
# obj.output()#using object we call the method



# class nav():
#     a=10#attribute
#     def display(self):
#         print(self.a)
# sai=nav()#object declaration
# #object name . method name()
# syam=nav()
# sai.display()
# syam.display()



#_int_
'''
constructor are generally used for instantiating an object.
the task of constructors is to initialize(assign values)
to the data members of the class when an object of the class is created.
in python the _int_() method is called the constructor and is always called when object is created
doesn't support multiple constructor
'''
#accessing other function variables by using init

# class sai():
#     def __init__(self,a,b,c):
#         self.ff=a
#         self.bb=b
#         self.cc=c
#         print(a)
#     def output(self):
#         print(self.ff,self.bb,self.cc) 
# p=sai(1,2,3)
# p.output()  




# class ramu():
#     def __init__(self,mobile_name,ram,battery,price):
#         self.a=mobile_name
#         self.b=ram
#         self.c=battery
#         self.d=price
#     def output(self):
#      print("mobile_name:",self.a)
#      print("ram:",self.b)
#      print("battery:",self.c)
#      print("price:",self.d)
# r=ramu("vivo","6gb","5000mh",10000)
# r.output()



#dynamically giving names

# class ramu():
#     def __init__(self,mobile_name,ram,battery,price):
#         self.a=mobile_name
#         self.b=ram
#         self.c=battery
#         self.d=price
#     def output(self):
#      print("mobile_name:",self.a)
#      print("ram:",self.b)
#      print("battery:",self.c)
#      print("price:",self.d)
# name=input("enter the mobile name:") 
# ramm=input("enter the mobile ram:")
# bat=input("enter the mobile battery:")
# price=input("enter the mombile price:")    
     
# r=ramu(name,ramm,bat,price)
# r.output()



# to use multiple mobiles using while loop

# class ramu():
#     def __init__(self,mobile_name,ram,battery,price):
#         self.a=mobile_name
#         self.b=ram
#         self.c=battery
#         self.d=price
#     def output(self):
#      print("mobile_name:",self.a)
#      print("ram:",self.b)
#      print("battery:",self.c)
#      print("price:",self.d)
# while True:
#     name=input("enter the mobile name:") 
#     ramm=input("enter the mobile ram:")
#     bat=input("enter the mobile battery:")
#     price=float(input("enter the mombile price:"))   
        
#     r=ramu(name,ramm,bat,price)
#     r.output()



# inheritance:
#single (parent child)
#multiple(two are more base classes)
#multilevel(tree)
#hierarchical(one base with sibling childs )


#single inheritance:

# class parent:
#     def output(self):
#         print("this is parent class")
# class child(parent):
#     def outputchild(self):
#         print('this is child class')
# i=child()
# i.output()
# i.outputchild()



#multiple inheriatance:

# class father:
#     def output(self):
#         print('this is parent class')
# class mother:
#     def outputm(self):
#         print('this is mother class')
# class child(father,mother):
#     def outputchild(self):
#         print('this is child')
# i=child()
# i.output()
# i.outputm()
# i.outputchild()



#multilevel inheritance:

# class grandFather:
#     def output(self):
#         print('this is gf class')
# class father(grandFather):
#     def outputf(self):
#         print('this is father class')
# class child(father):
#     def outputc(father):
#         print('this is child class')
# k=child()
# k.output()
# k.outputf()
# k.outputc()



# hierarchical inheritance:  

# class father:
#     def output(self):
#         print('this is father class')
# class child1(father):
#     def outputc(self):
#         print('this is child 1 class')
# class child2(father):
#     def outputcc(self):
#         print('this is child 2 class')
# i=child1()
# k=child2()
# i.output()
# i.outputc()
# k.output()
# k.outputcc()


#example pg of inhertances
# class Father:
#     def output(self):
#         print('this is father class')
# class Child1(Father):
#     def outputf(self):
#         print('this is child 1 class')
# obj=Child1()
# obj.outputf()



#ex pg
# class Father:
#     def funv(self):
#         print('this is father')
# class mother:
#     def fun(self):
#         print('this is mother')
# class done:
#     def fun2(self):
#         print('this is class')
# class child(Father,mother,done):
#     def func(self):
#         print('this is child')
# o=child()
# o.funv()
# o.fun()
# o.func()
# o.fun2()




'''polymorphism:
poly-many
morph=forms
1.method overloading
2.method overridding'''


# ex:method overloading approach

# class methodoverlod:
#  #  def some(self,a,b,c):
#     def some(self,a=None,b=None,c=None):
#         print(a,b,c)
# l=methodoverlod()
# l.some(1,2,3)
# l.some(1,2)
# l.some(1)
# l.some()




#method overridding overcoming using super() can we slove
# by the help of super we access parent class properties into child class

# class methodoverrid:
#     def display(self):
#         print('this is parent class')
# class child(methodoverrid):
#     def display(self):
#         print('this is child class')
#         # super().display()
# i=child()
# i.display()




'''encapsulation
binding of class (methods and variables(attributes))
# public
# private__
# protected_
'''


#ex protected_

# class Gfather:
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class father(Gfather):
#     def display1(self):
#         print(self._y)
# class child2(father):
#     def display2(self):
#         print('child2',self._y)
# o=child2(12)
# o.display2()
# o.display1()


# ex private_

# class Gfather:
#     def __init__(self,a):
#         self.__y=a
#         print(self.__y)
# class father(Gfather):
#     def display1(self):
#         print(self.__y)
# class child(father):
#     def display2(self):
#         print("child2",self.__y)
# o=child(12)
# o.display2()
# o.display1()




'''local variable and global variable
local variable use within function only
global variable we can access  any where
'''
# a=10#global variable
# def fun():
#     b=20#local variable
#     print('this is function',b,a)
# fun()
# # print(b)
# print(a)





'''abstraction
abstract method there is no body
abstract base class can not create object
a class contain one or more abstract methods then it said to be a abstract base class(abc)'''


# from abc import ABC,abstractmethod
# class car(ABC):
#     @abstractmethod#decorator
#     def mileage(self):
#         pass
    
# class tesla(car):
#     def mileage(self):
#         print('the mileage is 30kmph')
# class suziki(car):
#     def mileage(self):
#         print('the mileage is 25kmph')
# class duster(car):
#     def mileage(self):
#         print('the mileage is 24kmph')
# class renault(car):
#     def mileage(self):
#         print('the mileage is 27kmph')

# t=tesla()
# t.mileage()
# r=renault()
# t.mileage()
# s=suziki()
# s.mileage()
# d=duster()
# d.mileage()
