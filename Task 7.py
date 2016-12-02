""" Task 7
Write a recursive function (pseudocode and code) to check if a num. n is prime
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
    IF P1 LESS THAN 2
            PRINT (parametre1,'is invalid.')
    ELSE IF P1 EQUAL  2
            PRINT (parametre1, "is a prime.")
    ELSE
        IF P1 MOD P2 EQUAL 0
            PRINT (parametre1, 'is Not a Prime.')
        ELSE IF P1 MOD P2 NOT EQUAL 0 AND P2 NOT EQUAL 2
            optimusPrime(P1, P2 - 1)
        ELSE IF P1 MOD P2 NOT EQUAL 0 AND P2 EQUAL 2
            PRINT (parametre1, "is a Prime!")

Call the funtion with the parametres
"""
