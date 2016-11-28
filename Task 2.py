"""TASK 1: Question 2
Count the number of trailing 0s (number of 0s at the end of the number)
in a factorial number. Input: 5 Output: 1, Input: 10 Output: 2
Hint: Count the prime factors of 5"""

#get input factorial number from user
f = int(input("Enter a factorial number you want to trail zeros for: "))

def tailingZeros(f):#function defined containing users factorial number
    a = 1 # defining that a is 1 
    result = 0
    while f >= a: # if f is greater or equal to a 
        a *= 5
        result += f//a  # (floor divide)
    return result

# elegant print statement
print(str(f) + " has " + str(tailingZeros(f)) + " trailing zeros.")

#log n or linear
