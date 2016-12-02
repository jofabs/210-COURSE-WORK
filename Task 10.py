"""Question 10
Given a sequence of n integer numbers, extract the
sub-sequence of maximum length which is in ascending order."""



integers =[13,12,93,96,97,3,13,19,95,120,20,21,12,2,6,12,2016] #array of intergers
store = [] #Storing list
def sequence(integers, store):
    total = 1
    """Going through the list determining if the next integer is less than
    if it is then update the total by adding 1"""
    for s in range(len(integers)-1):
        if integers[s] < integers[s+1]:
            total = total + 1
        else:
            store.append(total)
            total = 1

    store.append(total)
    print(integers)
    print(store)
    print("The maximum subsequence of the given array in ascending order is - " + str(max(store)) + ".")

    """The following is an additional step to display integers of the maximum subsequence
    I am keep it as comment unless required"""
 #   highestSubseq = store.index(max(store))
 #   highestSub = max(store)
 #   totalSUM = 0
 #   for s in range(0, highestSubseq): 
 #       totalSUM = totalSUM + store[s]
 #   return("The maximum subsequence in ascending order is - " + str((integers)[totalSUM:totalSUM + highestSub]) + ".")
    

sequence(integers, store)
#print(sequence(integers, store))
