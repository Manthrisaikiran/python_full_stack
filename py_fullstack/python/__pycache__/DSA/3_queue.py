'''queue:
    
→queue is liner data structure

→it follows FIFO(first in first out)

→insertion of element is called 'rear'(enqueue)

→deletion of element is called 'front'(dequeue)

→time complexity O(1)'''

class queue(object):
    def __init__(self):
        self.queue=[]
    def isempty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.insert(0,data)
        return '{} added to queue'.format(data)
    def dequeue(self):
        return self.queue.pop()
    def sizequeue(self):
        return '{} size of queue'.format(len(self.queue))
    
if __name__=='__main__':
 q=queue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print("............................")
print(q.dequeue())
print(q.dequeue())
print(".............................")
print(q.sizequeue())
print(".............................")
print(q.isempty())
    
