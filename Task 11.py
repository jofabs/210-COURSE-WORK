"""Question 11
Based on the Python code or the C++ code provided in class as a starting point,
implement the binary search tree node delete function."""

class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
            self.head=None
            self.tail=None
      def insert(self,n,x):
          
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))


      def deleteNode(self, N): #Node delete function
            if N.prev != None:
                  N.prev.next = N.next
            else:
                  self.head = N.next
            if N.next !=0:
                  N.next.prev = N.prev
            else:
                  self.tail = N.prev


      #Time Complexity O(1)

            
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(5))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(7))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(9))
      l.deleteNode(l.head) #Performing the delete node, deleting the first node
      l.display()
