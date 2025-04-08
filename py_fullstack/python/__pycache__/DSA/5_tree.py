'''TREE

A tree is an abstract model and can be defined as a collection of entities called nodes linked together through edges in a hierarchical structure. 
They don't have any cyclic relations and there is only one path to a particular node.


Tree data structures have terminology that is worth becoming familiar with:

Root: the top (initial) node of the tree, where all the operations start

Node: each item in the tree, usually a key-value

Edge: a tree has n-1 edges (where n is the number of nodes) representing the connection between two nodes

Parent: a node which is a predecessor of any node

Child: a node which is descendant of any node

Siblings: a group of nodes which have the same parent

Leaf (terminal) node: a node without children

Level: it is defined as 1 + the number of edges between the node and the root

Height: the number of edges from its root to the furthest leaf

Depth: the number of edges from the node to the tree's root

Sub-tree: a portion of a tree data structure that can be viewed as a complete tree in itself


There are different types of trees that you can work with, like Binary Tree, Binary Search Tree, Red-Black tree, AVL tree, Heap, etc. 
The deciding factor of which tree type to use is performance.
Since trees are data structures, performance is measured in terms of inserting and retrieving data.'''

class treenode:
    def __init__(self,data):
        self.data=data
        self.childern=[]
        self.parent=None
    
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level=+1
            p=p.parent
        return level
    
    def printtree(self):
        spaces=' '*self.get_level()*3
        prefix=spaces+'|__'  if self.parent else ' '
        print(prefix+self.data)
        if self.childern:
            for child in self.childern:
                child.print_tree()
        
    def add_child(self,child):
        child.parent=self
        self.childern.append(child)
    
def build_tree():
    root=treenode('tollywood')
    heroin=treenode('heroins')
    heroin.add_child(treenode('samanth'))
    heroin.add_child(treenode('anushka'))
    heroin.add_child(treenode('tamanna'))
    heroin.add_child(treenode('pooja'))
     
    
    hero=treenode('hero')
    hero.add_child(treenode('pavan'))
    hero.add_child(treenode('prabhas'))
    hero.add_child(treenode('allu arjun'))
    hero.add_child(treenode('mahesh'))
     
     
    comedian=treenode('comedian')
    comedian.add_child(treenode('brammi'))
    comedian.add_child(treenode('alli'))
    comedian.add_child(treenode('ramu'))
    comedian.add_child(treenode('raju'))
     
    root.add_child(heroin)
    root.add_child(hero)
    root.add_child(comedian)
    root.printtree()

if __name__=='__main__':
    build_tree()

     
     
    