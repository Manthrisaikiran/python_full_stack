'''stack:

it is a liner data structure

it follow LIFO(last in first out)

new element is address at one end and remove at that end 

insert an element is called push

delete operation is called 'pop'

time complexity O(1)'''

# class stack(object):
#     #constructor
#     def __init__(self):
#      self.stack=[]
#      self.numitems=0
#     #checking empty
#     def isempty(self):
#         return self.stack==[]
#     #pushing element
#     def push(self,data):
#         self.stack.insert(self.numitems,data)
#         self.numitems+=1#increment index
#         return'{} pushed to stack'.format(data)
#     #deleting the element
#     def pop(self):
#         self.numitems-=1
#         data=self.stack.pop(self.numitems)
#         return '{} pop to stack'.format(data)
#     def stacksize(self):
#         return len(self.stack)
#     #testing
# if __name__=='__main__':
#   s=stack()
#   print(s.push(2))
#   print(s.push(8))
#   print(s.push(3))
#   print(s.push(9))
#   print('......................................')
#   print(s.pop())
# #   print(s.pop())
#   print('......................................')
#   print('size of stack',s.stacksize())