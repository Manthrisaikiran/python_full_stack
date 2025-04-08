'''What is Tuple?

1. Tuples are used to store multiple items in a single variable.

2. Tuples are written with round brackets () .

3. Unchangeable

4. A tuple is a collection which is unchangeable(Immutable). meaning that we cannot change, add or remove items after the tuple has been created.

5. Allow Duplicates


**Where tuples is used in Real time?

1. You can use a Tuple to store the latitude and longitude of your home, because a tuple always has a predefined number of elements (in this specific example, two). The same Tuple type can be used to store the coordinates of other locations

2. Tuples are faster than lists.

3. Tuples make the code safe from any accidental modification'''


# mohon=(1,22,2,22,43)
# print(mohon[1])


#tuple operations or tuple built in function....

# mohan=(1,22,2,22,43.33)
# print(max(mohan))
# print(min(mohan))
# print(sum(mohan))
# print(len(mohan))

# mohan=(1,22,2,22,43.33)#converting list..
# print(list(mohan))



# t1=(1,2,3)
# t2=(4,5,6)
# # print(t1+t2)
# s=zip(t1,t2)
# print(tuple(s))



# t1=(1,2,3)
# t2=(4,5,6)
# for i,j in zip(t1,t2):
#     print(i+j)


# t1=(1,2,3)
# t2=(4,5,6)
# new=[]
# for i,j in zip(t1,t2):
#     new.append(i+j)
#     print(tuple(new))



# d=(1,2,3)
# print(d*10)


# #membership operator....

# d=(2,3,4,5,6,7,7,87,88,8)
# # print(2 in d)
# print(22 not in d)



# identity operator......
# t1=(1,2,3)
# t2=(4,5,6,7,8)
# print(t1 is t2)


# t1=(1,2,3)
# t2=(1,2,3,4)
# print(t1 is not t2)


# t1=(1,2,3)
# t2=(1,2,3,)
# print(t1 is t2)


#.................................
# d=(1,2,3,35,4,6,7,8)
# for i in d:
#     print(i)



#atm........example pg
"""
s='''
    1.credit
    2.debit
    3.mini statement
    4.exit
  '''
amount=1000
name="kiran"
password="123"
user_name=input("enter the user name:")
passwords=input("enter the password name:")
if name==user_name and password==passwords:
    
    while True:
        print(s)
        option=int(input("enter the option:"))
        if option==1:
            credit_amount=float(input("enter the amount:"))
            print("amount after credit:",amount+credit_amount)
        elif option==2:
            debit_amount=float(input("enter the debit amount:"))
            print("amount after debit:",amount-debit_amount)
        elif option==3:
            print("total Amount:",amount)
        elif option==4:
            break
        
else:
    print("incorrect")
"""