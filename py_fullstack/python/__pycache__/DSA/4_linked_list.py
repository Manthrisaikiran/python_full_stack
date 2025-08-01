class Node(object):
    def __init__(self,d,n=None):
        self.data=d
        self.next_node=n
    def get_next(self):
        return self.next_node
    def set_next(self,n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self):
        self.data=d
    
class linkedlist(object):
    def __init__(self,r=None):
     self.root=r
     self.size=0
    def get_size(self):
        return self.size
  
    def add(self,d):
        new_node= Node(d,self.root)
        self.root = new_node
        self.size += 1
    
    def remove(self,d):
        this_node = self.root
        prev_node = None
    
        while this_node:
            if this_node.get_data()==d:
                if prev_node:
                 prev_node.set_next(this_node.get_next())
                else:
                 self.root = this_node.get_next()
                self.size -= 1
                return True #data removed
            else:
             prev_node = this_node
             this_node = this_node.get_next()
        return False #data not found
obj=linkedlist()
obj.add(5)
obj.add(8)
obj.add(19)
print('size'+str(obj.get_size()))
obj.remove(8)
print('size'+str(obj.get_size()))
obj.remove(8)
print('size'+str(obj.get_size()))
         
            
    
       
    
    
        
            