"""TASK 14
Implement BFS and DFS traversals for the above graph.
Save the nodes traversed in sequence to a text file."""


class vertex(): #Class definition
    def __init__(self,value):#function definition
        self.value = value
        self.adjacentlist = []

    def edgeaddition(self,vertex): #function definition
        self.adjacentlist.append(vertex)
        vertex.adjacentlist.append(self)


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

#Depthfirstsearch funtion pseudocode based 
    def depthfirstsearch(G,v): #passing a node object v 
        S = []
        visited = []
        S.append(v)
        while len(S) != 0:
            U = S.pop()
            if U.value not in visited:
                visited.append(U.value)
                for e in U.adjacentlist:
                    S.append(e)
        return visited

#Breathfirstsearch funtion pseudocode based
    def breathfirstsearch(G,v): #passing a node object v 
        Q = []
        visited = []
        Q.insert(0,v)
        while len(Q) !=0:
            U = Q.pop()
            if U.value not in visited:
                visited.append(U.value)
                for e in U.adjacentlist:
                    Q.insert(0,e)
        return visited

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
    
    #printing the items AND creating text file to store sequences
    d.printing()
    print("Locate 'output.txt' file for the for the traversed text file.")
    print("Depth First Search :", d.depthfirstsearch(nodeA), file=open("output.txt", "a"))
    print("Breath First Search :", d.breathfirstsearch(nodeA), file=open("output.txt", "a"))

    f = open("output.txt","r")
    text = f.read()
    f.close()
