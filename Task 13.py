"""TASK 13
Write the pseudocode for an unweighted graph data structure.
You either use an adjacency matrix or an adjacency list approach.
Also, write a function to add a new node and a function to add an edge.
Following that,implement the graph you have designed in python.
You may use your own linked list from previous labs, the STL LL,
or use a simple fixed size array (10 elements would be fine)."""


class vertex(): #Class definition
    def __init__(self,value):#function definition
        self.value = value
        self.adjacentlist = []

    def edgeaddition(self,vertex): #function definition
        self.adjacentlist.append(vertex)
        vertex.adjacentlist.append(self)#linking the nodes


class Graph(): #Class definition
    def __init__ (self):#function definition
        self.listofnodes = []

    def nodeaddition (self,value):#function definition
        self.listofnodes.append(vertex(value))#appenging the node to list
        return self.listofnodes[-1]
        
    def printing(self):#function definition
        for items in self.listofnodes:
            print(items.value, ":", end='')
            for m in items.adjacentlist:
                print(str(m.value),end='')
            print() #displays items of the graph eg: L:LL 

if __name__ == '__main__':
    #perfoming node addition
    print("The graph structure is:")

    d = Graph()
    #10 items(elements) 
    nodeA = d.nodeaddition('A')
    nodeL = d.nodeaddition('L')
    nodeE = d.nodeaddition('E')
    nodeX = d.nodeaddition('X')
    nodeV = d.nodeaddition('V')
    nodeI = d.nodeaddition('I')
    nodeC = d.nodeaddition('C')
    nodeT = d.nodeaddition('T')
    nodeO = d.nodeaddition('O')
    nodeR = d.nodeaddition('R')
    nodeV.edgeaddition(nodeA)
    nodeI.edgeaddition(nodeL)
    nodeC.edgeaddition(nodeE)
    nodeT.edgeaddition(nodeX)
    nodeO.edgeaddition(nodeV)
    nodeR.edgeaddition(nodeI)
    nodeA.edgeaddition(nodeC)
    nodeL.edgeaddition(nodeT)
    nodeE.edgeaddition(nodeO)
    nodeX.edgeaddition(nodeR)
    #printing the items
    d.printing()


"""
#PSEUDOCODE

CLASS VERTEX()
        value <- 0
        adjacentlist = []

    EDGEADDITION(VERTEX):
        APPEND THE VERTEX TO THE adjacentlist

CLASS GRAPH()
    listofnodes <- []

    FUNCTION NODEADDITION(VERTEX)
        APPEND VALUE OF VERTEX TO listofnodes

    FUNCTION PRINTING()
        FOR ITEMS IN LISTOFNODES
            DISPLAY THE VALUE OF ITEMS
            FOR EDGE IN adjacentlist OF ITEMS
                DISPLAY EDGE
        END FOR

d <- Graph
nodeA <- d.NODEADDITION('A')
nodeA.EDGEADDITION(nodeA)
d.PRINTING()           
"""
