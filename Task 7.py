""" Task 7
#Write a recursive function (pseudocode and code) to check if a num. n is prime
(hint: check whether n is divisible by any number below n)."""


parametre1 = int(input("Please enter a number to check if its a prime: "))
parametre2 = parametre1 - 1

def optimusPrime(p1, p2):#Recursive function definition with parametre's
    if p1 < 2:# Defining that 0,1, or negatives are not primes
            print (parametre1,'is invalid.')
    elif p1 == 2:# Defining that 2 is actually a prime
            print (parametre1, "is a prime.")
    else:
        if p1 % p2 == 0: #if the modulo of p1 and p2 equal 0 then its not prime
            print (parametre1, 'is Not a Prime.')
        elif p1 % p2 != 0 and p2 != 2:#if the modulo of p1 and p2 not equal 0 and p2 not equal 2
            #then its a prime
            optimusPrime(p1, p2 - 1)
        elif p1 % p2 != 0 and p2 == 2:#if the modulo of p1 and p2 not equal 0 and p2 is not 2
            #then its a prime
            print (parametre1, "is a Prime!")

optimusPrime(parametre1, parametre2)


"""PSEUDOCODE

parametre1 <- INPUT
parametre2 <- parametre1 - 1

OPTIMUSPRIME(P1, P2)
    if P1 LESS THAN 2
            print (parametre1,'is invalid.')
    else if P1 EQUAL  2
            print (parametre1, "is a prime.")
    else
        if P1 mod P2 EQUAL 0
            print (parametre1, 'is Not a Prime.')
        else if P1 mod P2 NOT EQUAL 0 and P2 NOT EQUAL 2
            optimusPrime(P1, P2 - 1)
        else if P1 mod P2 NOT EQUAL 0 and P2 EQUAL 2
            print (parametre1, "is a Prime!")

Call the funtion with the parametres
"""
