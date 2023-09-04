import sys
import os
 
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
 
 
class LinkedList:
     
    def __init__(self):
        self.Head = None
        self.size = 0
         
    def insert_node_to_tail(self, node):
         
        if node == None:
            return
          
        if self.is_empty() == True:
            self.Head = node
            self.Head.next = None
        else:           
            mytail = self.tail()        
            mytail.next = node
             
        self.size = self.size + 1
                         
    def insert_node_to_head(self, node): 
         
        if node == None:            
            return
         
        save_node = self.Head
        self.Head = node
        self.Head.next = save_node
         
        self.size = self.size + 1
                                   
    def is_empty(self):
         
        if self.size == 0:
            return True
        else:
            return False
 
    def head(self):  
         
        return self.Head
 
    def tail(self):     
         
        nodeiterator = self.Head
         
        while nodeiterator.next != None:
            nodeiterator = nodeiterator.next
         
        return nodeiterator
         
    def pop_left(self):
        if self.is_empty() == False:
            svnext = self.Head.next
 
            del self.Head 
            self.Head = None
            self.Head = svnext 
            self.size = self.size - 1
             
    def pop_right(self):
     
        nodeiterator = self.Head
        mytail = self.tail()
         
        if self.Size() == 1:
            self.Head = None
            del self.Head
            self.size = 0
            return
             
        while nodeiterator.next != mytail:
            nodeiterator = nodeiterator.next
        del nodeiterator.next
        nodeiterator.next  = None
        self.size = self.size - 1           
         
    def debugme(self):
        nodeiterator = self.Head
         
        while nodeiterator!= None:                       
            if nodeiterator.next != None:
                print("[{}]->".format( nodeiterator.value ), end= " ")
            else:
                print("[{}]".format( nodeiterator.value ), end= " ")
            nodeiterator = nodeiterator.next
        print("\n")
         
    def Size(self):
        return self.size
         
class Queue:
 
    def __init__(self):
        self.myque = LinkedList()
         
    def push(self,value):
        n = Node(value)
        self.myque.insert_node_to_tail( n )
     
    def first(self):
        n = self.myque.head()
        return n.value
     
    def pop(self):
        if self.myque:
            self.myque.pop_left()
             
    def Size(self):
        return self.myque.Size()
         
class Stack:
 
    def __init__(self):
        self.stack = LinkedList()
         
    def push(self,value):
        n = Node(value)
        self.stack.insert_node_to_head( n )
     
    def back(self):
        n = self.stack.tail()
        return n.value
     
    def pop(self):
        if self.stack:
            self.stack.pop_right()
             
    def Size(self):
        return self.stack.Size()
         
 
   
def testLinkedList():  
 
    print("Testing my Linked list")
     
    L2 = LinkedList()
    L2.insert_node_to_head(Node("head"))
    L2.insert_node_to_tail(Node("node1"))
    L2.insert_node_to_tail(Node("node2"))
    L2.insert_node_to_tail(Node("node3"))
    L2.insert_node_to_tail(Node("node3"))
    L2.insert_node_to_tail(Node("node4"))
    L2.insert_node_to_tail(Node("node3"))
    L2.insert_node_to_tail(Node("tail"))
    L2.insert_node_to_tail(Node("new tail"))
    L2.insert_node_to_head(Node("new head"))
    L2.debugme()
     
def testQueue():
     
    print("Testing my queue")
     
    Q = Queue()
    Q.push(1)
    Q.push(2)
    Q.push(3)
     
    size = Q.Size()
     
    for i in range(0,size):
        print("Element is: {}".format(Q.first()))
         
    for i in range(0,size):
        Q.pop()
 
def testStack():
 
    print("Testing my stack")
     
    S = Stack()
    S.push(1)
    S.push(2)
    S.push(3)
     
    size = S.Size()
     
    for i in range(0,size):
        print("Element is: {}".format(S.back()))
         
    for i in range(0,size):
        S.pop()
         
def main(argv):
    testQueue()
    testStack()
     
     
 
if __name__ == '__main__':
    main(sys.argv) 