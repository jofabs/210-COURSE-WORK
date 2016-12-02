"""TASK 6: Write the pseudocode and code for a function that reverses
the words in a sentence. Input: "This is awesome" Output: "awesome is This".
Give the Big O notation.
"""

q = input("Enter the word or sentence you want to reverse :")
def rev(q):
  y = q.split(" ") #list of elements in q(string)
  x = [] #empty list
  if q =="":
    return q
  else:
    for i in range(len(y)-1,-1,-1):#counter for which counts backwards 2,1,0
      x.append(y[i])#appends elements     
    return (' '.join(x))
      
print ("When you reverse your elements you get:", rev(q), ".")

"""BIG O NOTATION = O(n)"""

#Other solution is to use the reversed funtion
#' '.join(reversed(q.split()))
# FULL SOLUTION
#else:
#  return ' '.join(reversed(q.split()))


"""PSEUDOCODE

Q <- input("Enter the word or sentence you want to reverse :")
DEF REV(Q):
  Y <- split Q based on ""
  X <- []
  if Q ="":
    return Q
  else:
    for i = 0 to (lenght(Y)-1,-1,-1):
      append Y[i] to X    
    return (' '.join(x))
      
print (rev(q))
"""
