"""TASK 9
Adapt the binary search algorithm so that instead of outputting
whether a specific value was found, it outputs whether a value within
an interval (specified by you) was found. Write the pseudocode and code
and give the time complexity of the algorithm using the Big O notation.
Example input: L = [2,3,5,7,9,13] low= 10 high = 14 Output: True
"""

def alexBinarySearch(seq,low,high,start=0,end=-1): #Binarysearch algorithm
    if end==-1:
        end=len(seq)-1
    if start>end:
        return False
    if end==0 and seq[0]!=val:
        return False
    mid=int((start+end)/2)
    if seq[mid] <= high and seq[mid] >= low:
        return True
    elif high<seq[mid]:
        return alexBinarySearch(seq,low,high,start,mid-1)
    else:
        return alexBinarySearch(seq,low,high,mid+1,end)

    
seq=[1,2,3,4,5,6,7,8,9,10,30]
print(alexBinarySearch(seq,27,31))


"""BIG O NOTATION = O(log n) because it is logarithmic in finding the item
in the array """
